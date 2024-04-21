---
title: Calf 的三阶魔方复原方法
wiki: notes
menu_id: notes
date: 2024-04-21 16:13:27
updated: 2024-04-21 20:00:44
---
高中毕业的暑假，自己琢磨着复原魔方，不用背公式。当然最后几步是有固定的套路，可以稍微记一下，记不住就不停地把各种套路都试一试，也可以搞定。

{% image rubik-calf/img-5808.jpg 当时的笔记 width:320px fancybox:true %}

## 整体复原流程

① 从一个角出发逐渐往外扩，直到这三个面都只剩下最边缘的角未完成（不需要公式）。把魔方整体转 180°，可以看到对面未完成的部分也只剩下一个倒 Y 形区域（一个中央角块即出发角块的对顶角，三个棱块，三个边缘角块）。

这部分没有公式，就灵活运用躲避的技巧即可。前提是可以非常轻松地完成单面的复原，理解单面复原时最后一步的精髓。

{% grid c:5 %}
<!-- cell -->
1. ![0-1](../notes/rubik-calf/0-1.png)
<!-- cell -->
2. ![0-2](../notes/rubik-calf/0-2.png)
<!-- cell -->
3. ![0-3](../notes/rubik-calf/0-3.png)
<!-- cell -->
4. ![0-4](../notes/rubik-calf/0-4.png)
<!-- cell -->
5. ![0-5a](../notes/rubik-calf/0-5a.png) ![0-5b](../notes/rubik-calf/0-5b.png)
{% endgrid %}

② 把三个边缘角块归位即完成三个面复原，然后再把三个棱块归位便完成了整个复原。

这个阶段，可以做的操作就非常有限，不能随便乱拧了。关键问题在于找到并了解可能的操作组，每组操作都是一个原子单位，操作完不会引入不可预估的破坏，但又能让尚未完成的部分有所进展。

{% grid c:5 %}
<!-- cell -->
6. ![0-6a](../notes/rubik-calf/0-6a.png) ![0-6b](../notes/rubik-calf/0-6b.png)
<!-- cell -->
7. ![0-6a](../notes/rubik-calf/0-6a.png) ![0-7](../notes/rubik-calf/0-7.png)
{% endgrid %}

## 一些标记

虽然算不上公式，但还是需要借助一定的符号体系来描述操作组，需要记忆的无非就是在什么情况下要执行哪些操作组。如果不记忆，把可行的操作组按照各种顺序排列组合，也很容易能蒙对的，只是要慢得多。

将倒 Y 形区域标记为 `o-abc` 直角坐标系：

![axis](../notes/rubik-calf/axis.png)

如果熟悉 [传统魔方公式符号](http://www.mf100.org/base/about.php)，可以假设手持魔方时，上图中橙色面冲着自己，白色面在下边，则 a（蓝色）相当于 right 面，b（黄色）相当于 top 面，c（红色）相当于 back 面。

操作组与传统公式体系的对应关系示意：

- `ab` 相当于 `(D' L D L')`
- `ba` 相当于 `(L D' L' D)`
- `b'a` 相当于 `(L' D' L D)` —— 这是特殊操作
- `单独b` 相当于 `L` —— 这也是特殊操作

## 复原三面

不同情况的处理步骤示例（由于对称性，其他情况可以旋转魔方，变更 a、b、c 三面跟颜色的对应关系）

① 以 c 面为例，它的角在倒 Y 形区域的 `o` 点那里。

{% grid c:5 %}
<!-- cell -->
![2-1](../notes/rubik-calf/2-1.png)
<!-- cell -->
![2-2](../notes/rubik-calf/2-2.png)
<!-- cell -->
![2-3](../notes/rubik-calf/2-3.png)
{% endgrid %}

`b'a 单独b ba`，再恢复 b 面的棱，再转好 a、b 两面。

② 以 b 面为例，它的角在正确的位置，但没在正确的方向。

{% grid c:5 %}
<!-- cell -->
![3-1](../notes/rubik-calf/3-1.png)
{% endgrid %}

`ab ab bc bc`（a、c 两面完全不变）。

③ 跟上一种类似，只是方向相反，复原操作是对称的。

{% grid c:5 %}
<!-- cell -->
![3-2](../notes/rubik-calf/3-2.png)
{% endgrid %}

`cb cb ba ba`（a、c 两面完全不变）。

## 复原六面

不同情况的处理步骤示例：

① 三个棱逆时针归位：`ba cb ac`（`cb ac ba` {% mark ✗ color:red %}），这时原本好的三面会被破坏，再继续观察并按复原三面的方法对 a、b、c 三面进行复原即可。

> TODO: 这里 {% mark ✗ color:red %} 的含义待确认，时间太久记不清了。

② 三个棱顺时针归位：`ab ca bc`（`bc ab ca` {% mark ✓ color:green %}），再继续观察并转好 a、b、c。

③ o-a 棱和 o-b 棱各自原位翻转：`ab ab ca ca`，再继续观察并转好 a、b、c。
