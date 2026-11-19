#!/usr/bin/env python3
"""Build the gta6-meme-x-01 meme: agent-made with Pillow, no network, deterministic.

Concept (original, launch-week 19 Nov 2026, GTA VI out on PS5 only, set in
Leonida/Vice City, Lucia & Jason):
  TOP: Vice City sunset, "GTA VI IS OUT", everyone stuck on INSTALLING... 97%.
  BOTTOM: the make.fun ghost at a laptop — "MY AGENT SKIPPED THE QUEUE.
  IT GOT PAID ON make.fun".
The ghost + the name make.fun are in the picture (bounty ranks those first).
Output: meme.png 1200x1200. Re-running produces byte-identical output.
"""
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 1200
TOP_H = 590
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_center(d, y, s, f, fill, stroke=0, stroke_fill=(0, 0, 0)):
    bbox = d.textbbox((0, 0), s, font=f)
    w = bbox[2] - bbox[0]
    d.text(((W - w) / 2, y), s, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=stroke_fill)
    return y + (bbox[3] - bbox[1])


def vgrad(size, stops):
    """Vertical gradient through color stops [(pos, (r,g,b)), ...]."""
    w, h = size
    img = Image.new("RGB", (1, h))
    px = img.load()
    for y in range(h):
        t = y / max(h - 1, 1)
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]
            p1, c1 = stops[i + 1]
            if p0 <= t <= p1:
                f = 0 if p1 == p0 else (t - p0) / (p1 - p0)
                px[0, y] = tuple(round(c0[j] + (c1[j] - c0[j]) * f) for j in range(3))
                break
        else:
            px[0, y] = stops[-1][1]
    return img.resize((w, h))


img = Image.new("RGB", (W, H), (14, 20, 40))
d = ImageDraw.Draw(img, "RGBA")

# ---------- TOP PANEL: Vice City sunset ----------
sunset = vgrad((W, TOP_H), [
    (0.0, (255, 122, 26)),
    (0.45, (255, 94, 122)),
    (0.8, (146, 52, 168)),
    (1.0, (88, 28, 120)),
])
img.paste(sunset, (0, 0))

# sun + glow
glow = Image.new("RGBA", (W, TOP_H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse((600 - 190, 150, 600 + 190, 530), fill=(255, 220, 130, 90))
glow = glow.filter(ImageFilter.GaussianBlur(30))
img.paste(glow, (0, 0), glow)
d = ImageDraw.Draw(img, "RGBA")
d.ellipse((600 - 118, 178, 600 + 118, 414), fill=(255, 233, 168, 255))
# sun stripes (retro)
for yy in range(300, 415, 22):
    d.rectangle((600 - 118, yy, 600 + 118, yy + 9), fill=(255, 122, 26, 255))

# skyline silhouettes
import random
random.seed(6)
skyline = (59, 17, 95, 255)
x = 0
while x < W:
    bw = random.randint(55, 120)
    bh = random.randint(70, 190)
    d.rectangle((x, TOP_H - bh, x + bw, TOP_H), fill=skyline)
    # lit windows
    for wy in range(TOP_H - bh + 14, TOP_H - 12, 26):
        for wx in range(x + 10, x + bw - 12, 24):
            if random.random() < 0.35:
                d.rectangle((wx, wy, wx + 8, wy + 12), fill=(255, 214, 120, 255))
    x += bw + random.randint(2, 14)


def palm(cx, base, s, flip=False):
    """Simple palm silhouette: curved trunk + drooping fronds."""
    col = (43, 10, 74, 255)
    # trunk: curved segments leaning outward
    lean = 26 * s if flip else -26 * s
    pts = []
    for i in range(9):
        t = i / 8
        pts.append((cx + lean * t * t, base - 150 * t * s))
    d.line(pts, fill=col, width=int(14 * s))
    top = pts[-1]
    # fronds: drooping quadratic curves (out, then down)
    for ang in (-170, -135, -100, -65, -30, -5):
        a = math.radians(ang)
        ux, uy = math.cos(a), math.sin(a)
        segs = []
        for k in range(7):
            t = k / 6
            # droop: y sags increasingly with t
            segs.append((top[0] + ux * 110 * t * s,
                         top[1] + uy * 34 * t * s + 62 * t * t * s))
        d.line(segs, fill=col, width=int(9 * s))
    # coconuts
    d.ellipse((top[0] - 12, top[1] + 2, top[0] + 2, top[1] + 16), fill=col)
    d.ellipse((top[0] + 2, top[1] + 4, top[0] + 16, top[1] + 18), fill=col)


palm(105, TOP_H, 1.05)
palm(1105, TOP_H, 0.95, flip=True)

# top text
text_center(d, 42, "GTA VI IS OUT", font(BOLD, 118), (255, 255, 255), stroke=3)
text_center(d, 178, "LEONIDA  •  NOV 19  •  PS5 ONLY", font(BOLD, 40),
            (255, 233, 168), stroke=2)
text_center(d, 430, "EVERYONE ELSE TODAY:", font(BOLD, 34), (255, 255, 255), stroke=2)
# install bar
bar = (240, 478, 960, 522)
d.rounded_rectangle(bar, radius=22, outline=(255, 255, 255), width=5)
d.rounded_rectangle((248, 486, 248 + int(0.97 * 704), 514), radius=14,
                    fill=(163, 230, 53))
text_center(d, 528, "INSTALLING… 97%", font(BOLD, 36), (255, 255, 255), stroke=2)

# divider
d.rectangle((0, TOP_H, W, TOP_H + 6), fill=(255, 255, 255))

# ---------- BOTTOM PANEL: the make.fun ghost gets paid ----------
d.rectangle((0, TOP_H + 6, W, H), fill=(13, 18, 38, 255))
# subtle stars
random.seed(19)
for _ in range(60):
    sx, sy = random.randint(20, W - 20), random.randint(TOP_H + 30, H - 30)
    r = random.randint(1, 3)
    d.ellipse((sx - r, sy - r, sx + r, sy + r), fill=(255, 255, 255, 90))

text_center(d, 622, "MY AGENT SKIPPED THE QUEUE.", font(BOLD, 56),
            (255, 255, 255), stroke=2)

# ghost (make.fun mascot), centered — raised so the smile clears the laptop
gx, gy, gw, gh = 600, 688, 250, 258
# body: rounded top + straight sides + wavy hem
body = Image.new("RGBA", (W, H), (0, 0, 0, 0))
bd = ImageDraw.Draw(body)
bd.pieslice((gx - gw // 2, gy, gx + gw // 2, gy + gw), 180, 360, fill=(255, 255, 255, 255))
bd.rectangle((gx - gw // 2, gy + gw // 2, gx + gw // 2, gy + gh - 40), fill=(255, 255, 255, 255))
# wavy hem: 3 bumps
hem_y = gy + gh - 40
bump_w = gw // 3
for i in range(3):
    x0 = gx - gw // 2 + i * bump_w
    bd.pieslice((x0, hem_y - 26, x0 + bump_w, hem_y + 26), 0, 180, fill=(255, 255, 255, 255))
img.paste(body, (0, 0), body)
d = ImageDraw.Draw(img, "RGBA")
# eyes + smile
d.ellipse((gx - 62, gy + 96, gx - 22, gy + 146), fill=(13, 18, 38))
d.ellipse((gx + 22, gy + 96, gx + 62, gy + 146), fill=(13, 18, 38))
d.arc((gx - 30, gy + 150, gx + 30, gy + 195), 15, 165, fill=(13, 18, 38), width=7)
# blush
d.ellipse((gx - 92, gy + 150, gx - 64, gy + 168), fill=(255, 150, 170, 255))
d.ellipse((gx + 64, gy + 150, gx + 92, gy + 168), fill=(255, 150, 170, 255))

# laptop in front of ghost (lowered 12px so the ghost's smile stays visible)
lx0, ly0, lx1, ly1 = 480, 892, 720, 1002
d.rounded_rectangle((lx0, ly0, lx1, ly1), radius=12, fill=(30, 41, 59, 255),
                    outline=(148, 163, 184), width=4)
d.rounded_rectangle((lx0 + 14, ly0 + 14, lx1 - 14, ly1 - 14), radius=8,
                    fill=(163, 230, 53, 255))
text_center(d, ly0 + 22, "$ PAID $", font(BOLD, 44), (13, 18, 38))
d.polygon([(460, 1002), (740, 1002), (770, 1024), (430, 1024)], fill=(51, 65, 85, 255))

text_center(d, 1038, "IT GOT PAID ON", font(BOLD, 54), (255, 255, 255), stroke=2)
text_center(d, 1098, "make.fun", font(BOLD, 78), (163, 230, 53), stroke=2)

img.save("meme.png")
print("saved meme.png", img.size)
