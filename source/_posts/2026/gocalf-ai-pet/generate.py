"""Generate gocalf desktop pet animations from the logo design.

The logo is a stylized blue calf:
- a thick C-shape (body/face outline) on a transparent background
- two small horn-like shapes on top

We compose each frame in an SVG (viewBox 0..32) inspired by the original logo,
then add eyes / mouth / props per state and per frame. Frames are rasterized via
cairosvg, packed onto a transparent 352x352 canvas, and saved as animated WebP.

Body bigger (VIEW=44), eyes (sclera+pupil) on top arc, mouth on bottom arc,
larger pink cheeks below eyes.
"""

import io
import math
from pathlib import Path

import cairosvg
from PIL import Image

OUT_DIR = Path(__file__).parent
STICKERS_DIR = OUT_DIR / "stickers"
STICKERS_DIR.mkdir(exist_ok=True)

TARGET = 352
VIEW = 44
BLUE = "#3370FF"
DARK = "#1F2A44"
WHITE = "#FFFFFF"
PINK = "#FF8FB1"
YELLOW = "#FFC93C"

# ---------- body ----------

def calf_body(dx=0, dy=0, scale=1.0, squash=1.0, rot=0):
    cx_local, cy_local = 14, 15.5
    tx, ty = VIEW / 2 + dx, VIEW / 2 + dy
    parts = [f"translate({tx} {ty})"]
    if rot:
        parts.append(f"rotate({rot})")
    parts.append(f"scale({scale} {scale * squash})")
    parts.append(f"translate({-cx_local} {-cy_local})")
    t = " ".join(parts)
    return f'''<g transform="{t}">
  <g transform="translate(2 0.3)" fill="{BLUE}">
    <path fill-rule="nonzero" d="M14,2.92 C16.5194671,2.92 18.8834923,3.58552618 20.9258646,4.75036765 C23.3266591,6.11963072 25.2829988,8.17883964 26.5249111,10.6580218 L21.157438,13.3424173 C19.8441878,10.7201917 17.1323226,8.92 14,8.92 C9.581722,8.92 6,12.501722 6,16.92 C6,21.338278 9.581722,24.92 14,24.92 C17.1319237,24.92 19.8434972,23.1202667 21.1569362,20.4985844 L26.524486,23.1828269 C24.2259103,27.770606 19.4807453,30.92 14,30.92 C6.26801351,30.92 0,24.6519865 0,16.92 C0,9.18801351 6.26801351,2.92 14,2.92 Z"/>
    <path d="M3.5,0.52 C4.04,0.52 4.51,0.80 4.78,1.23 L4.79,1.25 C4.84,1.33 4.88,1.41 4.91,1.50 C5.67,2.98 7.22,4 9,4 C9.64,4 10.25,3.87 10.80,3.63 C11.44,5.13 12.13,6.88 12.57,7.95 C11.52,8.56 10.30,8.92 9,8.92 C5.18,8.92 2.07,5.86 2.00,2.06 L2,2.02 C2,1.19 2.67,0.52 3.5,0.52 Z"/>
    <path transform="translate(20.68, 4.72) scale(-1, 1) translate(-20.68, -4.72)" d="M16.9,0.52 C17.44,0.52 17.91,0.80 18.18,1.23 L18.19,1.25 C18.24,1.33 18.28,1.41 18.31,1.50 C19.07,2.98 20.62,4 22.4,4 C23.04,4 23.65,3.87 24.20,3.63 C24.84,5.13 25.53,6.88 25.97,7.95 C24.92,8.56 23.70,8.92 22.4,8.92 C18.58,8.92 15.47,5.86 15.40,2.06 L15.4,2.02 C15.4,1.19 16.07,0.52 16.9,0.52 Z"/>
  </g>
</g>'''


# ---------- face parts ----------

EYE_CY = 15.2
EYE_X1, EYE_X2 = 18.5, 25.5


def eyes(open_amt=1.0, look_dx=0, look_dy=0):
    pup_rx = 1.3
    pup_ry = max(0.25, 1.3 * open_amt)
    out = []
    for ex in (EYE_X1, EYE_X2):
        out.append(f'<ellipse cx="{ex}" cy="{EYE_CY}" rx="2.6" ry="2.6" fill="{WHITE}"/>')
        out.append(f'<ellipse cx="{ex+look_dx*0.6}" cy="{EYE_CY+look_dy*0.6}" rx="{pup_rx}" ry="{pup_ry}" fill="{DARK}"/>')
        if open_amt > 0.4:
            out.append(f'<circle cx="{ex+look_dx*0.6+0.4}" cy="{EYE_CY+look_dy*0.6-0.5}" r="0.45" fill="{WHITE}"/>')
    return "\n".join(out)


def eyes_happy_closed():
    """Smile-shaped closed eyes."""
    e1 = f'<path d="M {EYE_X1-1.6} {EYE_CY+0.4} Q {EYE_X1} {EYE_CY-1.6} {EYE_X1+1.6} {EYE_CY+0.4}" stroke="{WHITE}" stroke-width="0.9" fill="none" stroke-linecap="round"/>'
    e2 = f'<path d="M {EYE_X2-1.6} {EYE_CY+0.4} Q {EYE_X2} {EYE_CY-1.6} {EYE_X2+1.6} {EYE_CY+0.4}" stroke="{WHITE}" stroke-width="0.9" fill="none" stroke-linecap="round"/>'
    return e1 + e2


def eyes_sad():
    """Droopy half-lidded eyes for error state. Still uses sclera+pupil so
    they remain visible, but with a heavy upper lid arc covering the top."""
    out = []
    for ex in (EYE_X1, EYE_X2):
        out.append(f'<ellipse cx="{ex}" cy="{EYE_CY+0.2}" rx="2.6" ry="2.2" fill="{WHITE}"/>')
        # pupil low and small
        out.append(f'<ellipse cx="{ex}" cy="{EYE_CY+1.1}" rx="1.1" ry="0.8" fill="{DARK}"/>')
        # heavy droopy lid (arc above)
        out.append(f'<path d="M {ex-2.7} {EYE_CY+0.2} Q {ex} {EYE_CY-2.2} {ex+2.7} {EYE_CY+0.2}" stroke="{BLUE}" stroke-width="1.6" fill="{BLUE}"/>')
        # tiny brow above for emphasis
        out.append(f'<path d="M {ex-1.8} {EYE_CY-2.6} L {ex+1.8} {EYE_CY-1.6}" stroke="{DARK}" stroke-width="0.55" stroke-linecap="round"/>')
    return "\n".join(out)


def cheeks():
    return (f'<ellipse cx="16.5" cy="20.5" rx="2.0" ry="1.05" fill="{PINK}" opacity="0.9"/>'
            f'<ellipse cx="27.5" cy="20.5" rx="2.0" ry="1.05" fill="{PINK}" opacity="0.9"/>')


def mouth_smile(width=1.0):
    """Smile on bottom blue arc. width scales horizontal extent."""
    x1 = 22 - 2.4 * width
    x2 = 22 + 2.4 * width
    return (f'<path d="M {x1} 32.2 Q 22 34.1 {x2} 32.2" '
            f'stroke="{WHITE}" stroke-width="1.1" fill="none" stroke-linecap="round"/>')


def mouth_big_smile():
    return (f'<path d="M 19.0 31.6 Q 22 35.0 25.0 31.6" '
            f'stroke="{WHITE}" stroke-width="1.3" fill="none" stroke-linecap="round"/>')


def mouth_o(r=0.7):
    return f'<ellipse cx="22" cy="33.0" rx="{r*0.7}" ry="{r}" fill="{WHITE}"/>'


def mouth_frown():
    return (f'<path d="M 19.6 33.6 Q 22 31.8 24.4 33.6" '
            f'stroke="{WHITE}" stroke-width="1.1" fill="none" stroke-linecap="round"/>')


def sparkle(cx, cy, size=2, color=YELLOW, opacity=1.0):
    s = size
    return (f'<g opacity="{opacity}" transform="translate({cx} {cy})">'
            f'<path d="M 0 -{s} L {s*0.3} -{s*0.3} L {s} 0 L {s*0.3} {s*0.3} L 0 {s} L -{s*0.3} {s*0.3} L -{s} 0 L -{s*0.3} -{s*0.3} Z" fill="{color}"/>'
            f'</g>')


def tear(cx, cy, length=2.0, opacity=1.0):
    return (f'<path d="M {cx} {cy} Q {cx-0.55} {cy+length*0.5} {cx} {cy+length} Q {cx+0.55} {cy+length*0.5} {cx} {cy} Z" '
            f'fill="#5AB8FF" opacity="{opacity}"/>')


def svg_doc(inner: str) -> str:
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VIEW} {VIEW}">\n{inner}\n</svg>'


def render(svg_text: str) -> Image.Image:
    png = cairosvg.svg2png(bytestring=svg_text.encode("utf-8"),
                            output_width=TARGET, output_height=TARGET)
    return Image.open(io.BytesIO(png)).convert("RGBA")


# ---------- state frames ----------

def f_idle(t):
    squash = 1.0 + 0.018 * math.sin(t * 2 * math.pi)
    dy = -0.3 * math.sin(t * 2 * math.pi)
    bp = (t - 0.88) / 0.06
    open_amt = abs(0.5 - bp) * 2 if 0 <= bp <= 1 else 1.0
    return svg_doc("\n".join([calf_body(dy=dy, squash=squash), cheeks(),
                              eyes(open_amt), mouth_smile()]))


def f_idle2(t):
    rot = 3 * math.sin(t * 2 * math.pi)
    return svg_doc("\n".join([calf_body(rot=rot), cheeks(),
                              eyes(1.0), mouth_smile()]))


def f_thinking(t):
    rot = 7 * math.sin(t * 2 * math.pi)
    dy = -0.25 * abs(math.sin(t * 2 * math.pi))
    body = calf_body(dy=dy, rot=rot)
    dots = []
    for i in range(3):
        phase = (t * 3 - i) % 3
        active = phase < 1
        size = 1.4 if active else 1.0
        op = 1.0 if active else 0.4
        y_off = -1.5 if active else 0
        dots.append(f'<circle cx="{34+i*3}" cy="{8+y_off}" r="{size}" fill="{BLUE}" opacity="{op}"/>')
    # eyes look up + slightly right (toward dots)
    return svg_doc("\n".join([body, cheeks(), eyes(1.0, look_dx=0.6, look_dy=-0.5),
                              mouth_smile(width=0.8)] + dots))


def f_needs_input(t):
    look = math.sin(t * 2 * math.pi) * 0.9
    pulse = 1.0 + 0.18 * math.sin(t * 4 * math.pi)
    qm = (f'<g transform="translate(35 7) scale({pulse})">'
          f'<text x="0" y="0" font-family="Helvetica, Arial, sans-serif" font-weight="900" font-size="8" '
          f'text-anchor="middle" dominant-baseline="middle" fill="{YELLOW}" stroke="{DARK}" stroke-width="0.5" paint-order="stroke">?</text>'
          f'</g>')
    return svg_doc("\n".join([calf_body(), cheeks(),
                              eyes(1.0, look_dx=look),
                              mouth_o(r=0.7), qm]))


def f_complete(t):
    bounce = -1.8 * abs(math.sin(t * 2 * math.pi))
    body = calf_body(dy=bounce, squash=1.0 + 0.035 * math.sin(t * 2 * math.pi))
    parts = [body, cheeks(), eyes_happy_closed(), mouth_big_smile()]
    for i in range(4):
        ang = t * 2 * math.pi + i * math.pi / 2
        cx = 22 + math.cos(ang) * 17
        cy = 22 + math.sin(ang) * 17
        size = 1.6 + 0.5 * math.sin(t * 2 * math.pi + i)
        parts.append(sparkle(cx, cy, size=size))
    return svg_doc("\n".join(parts))


def f_error(t):
    shake = math.sin(t * 8 * math.pi) * 0.35
    body = calf_body(dx=shake)
    tear_y = 18 + (t * 8) % 8
    tear_op = 1.0 if (t * 8) % 8 < 6 else max(0, 1 - ((t * 8) % 8 - 6) / 2)
    parts = [body, cheeks(), eyes_sad(), mouth_frown(),
             tear(20.3, tear_y, length=1.8, opacity=tear_op)]
    return svg_doc("\n".join(parts))


# ---------- compose ----------

def build(name, fn, n_frames, duration_ms):
    frames = [render(fn(i / n_frames)) for i in range(n_frames)]
    out = STICKERS_DIR / f"{name}.webp"
    frames[0].save(out, save_all=True, append_images=frames[1:],
                   duration=duration_ms, loop=0, lossless=True, format="WEBP")
    # also save first-frame preview
    frames[0].save(OUT_DIR / f"preview_{name}.png")
    print(f"wrote {out}")


def main():
    build("idle-1", f_idle, 30, 80)
    build("idle-2", f_idle2, 24, 100)
    build("thinking-1", f_thinking, 24, 90)
    build("needs_input-1", f_needs_input, 20, 90)
    build("complete-1", f_complete, 20, 80)
    build("error-1", f_error, 24, 80)


if __name__ == "__main__":
    main()
