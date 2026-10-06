#!/usr/bin/env python3
"""Render an inspectable chart JSON to a static SVG. Python 3.11+ standard library.
Usage: python3 render.py chart.json chart.svg
No JavaScript, external resources, executable templates, smoothing or resampling.
Decimal arithmetic preserves the supplied coordinates; SVG coordinates use 6 decimals.
"""
import json, sys
from decimal import Decimal as D
from pathlib import Path
import xml.etree.ElementTree as E

NS='http://www.w3.org/2000/svg'
E.register_namespace('',NS)
def render(config):
    w,h=config['size']; left,right,top,bottom=64,w-25,65,h-90
    plotw,ploth=right-left,bottom-top
    root=E.Element('{'+NS+'}svg',{'viewBox':f'0 0 {w} {h}','width':str(w),'height':str(h),'role':'img','aria-labelledby':'title desc'})
    def add(tag,attrs=None,text=None):
        el=E.SubElement(root,'{'+NS+'}'+tag,{k:str(v) for k,v in (attrs or {}).items()})
        if text is not None: el.text=str(text)
        return el
    add('title',{'id':'title'},config['title'] or config['accessible_title'])
    add('desc',{'id':'desc'},'Static chart. Exact original data are supplied in the accompanying JSON; no interactive tooltips.')
    add('rect',{'width':w,'height':h,'fill':'#fff'})
    def text(x,y,value,size=12,anchor='middle',fill='#333'):
        return add('text',{'x':x,'y':y,'font-size':size,'text-anchor':anchor,'fill':fill,'font-family':'Arial, PingFang SC, Microsoft YaHei, sans-serif'},value)
    title=config['title'] or ''
    # Explicit wrapping only, without omitting text.
    lines=config.get('title_lines',[title])
    for i,line in enumerate(lines): text(w/2,22+19*i,line,15)
    ymin,ymax,step=map(D,map(str,config['y_range']))
    xmin,xmax=map(D,map(str,config['x_range']))
    def X(v): return float(D(left)+(D(str(v))-xmin)/(xmax-xmin)*D(plotw))
    def Y(v): return float(D(bottom)-(D(str(v))-ymin)/(ymax-ymin)*D(ploth))
    v=ymin
    while v<=ymax:
        y=Y(v);add('path',{'d':f'M {left} {y:.6f} H {right}','fill':'none','stroke':'#ddd','stroke-width':1})
        text(left-10,y+4,format(v.normalize(),'f'),11,'end');v+=step
    add('path',{'d':f'M {left} {top} V {bottom} H {right}','fill':'none','stroke':'#999'})
    if config['kind']=='line':
        if config.get('categories'):
            ticks=list(enumerate(config['categories']))
        else: ticks=[(D(i)/10,str(D(i)/10)) for i in range(11)]
        for x,label in ticks: text(f'{X(x):.6f}',bottom+20,label,11)
        for series,color in zip(config['series'],config['colors'],strict=True):
            points=series['data']
            xy=[(i,v) for i,v in enumerate(points)] if config.get('categories') else points
            assert all(ymin<=D(str(y))<=ymax and xmin<=D(str(x))<=xmax for x,y in xy)
            add('polyline',{'points':' '.join(f'{X(x):.6f},{Y(y):.6f}' for x,y in xy),'fill':'none','stroke':color,'stroke-width':2,'data-series':series['name']})
            for x,y in xy:
                add('circle',{'cx':f'{X(x):.6f}','cy':f'{Y(y):.6f}','r':3,'fill':color,'data-x':x,'data-y':y,'data-series':series['name']})
        legends=[s['name'] for s in config['series']]
    else:
        assert config['kind']=='variable-width'
        data=config['rawData'];gap=sum(D(str(v['x'])) for v in data)/D(len(data))*D(str(config['gap_ratio']))
        x=D(0)
        for v,color in zip(data,config['colors'],strict=True):
            width=D(str(v['x']));height=D(str(v['y']))
            add('rect',{'x':f'{X(x):.6f}','y':f'{Y(height):.6f}','width':f'{X(x+width)-X(x):.6f}','height':f'{Y(0)-Y(height):.6f}','fill':color,'fill-opacity':'.75','stroke':color,'data-series':v['name'],'data-left':x,'data-width':width,'data-height':height})
            text(f'{X(x+width/2):.6f}',f'{Y(height)-9:.6f}',f'{width} x {height}',12)
            x+=width+gap
        legends=[v['name'] for v in data]
    cols=5 if len(legends)>5 else len(legends)
    colw=(w-70)/cols
    for i,(label,color) in enumerate(zip(legends,config['colors'],strict=True)):
        x=45+(i%cols)*colw;y=h-45+(i//cols)*23
        add('path',{'d':f'M {x} {y} h 18','stroke':color,'stroke-width':3})
        text(x+25,y+4,label,12,'start')
    return E.tostring(root,encoding='unicode')+'\n'
if __name__=='__main__':
    assert len(sys.argv)==3, __doc__
    config=json.loads(Path(sys.argv[1]).read_text(),parse_float=D)
    Path(sys.argv[2]).write_text(render(config))
