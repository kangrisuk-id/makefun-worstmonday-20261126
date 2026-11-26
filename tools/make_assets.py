#!/usr/bin/env python3
"""Build-time visual assets for the Worst Monday One-Liners README.

Pillow is used ONLY here, at build time. main.py is pure stdlib and never
imports it. Run: python3 tools/make_assets.py  (writes assets/*.png)
"""
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")

BG = (22, 24, 29)        # deep charcoal
SURFACE = (32, 35, 43)   # layered surface
GOLD = (212, 169, 78)    # restrained gold
WHITE = (240, 238, 232)
MUTED = (168, 170, 178)
RED = (214, 92, 92)
GREEN = (96, 190, 120)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def base(w, h, title, kicker):
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, w, 6], fill=GOLD)
    d.rectangle([24, h - 24, w - 24, h - 23], fill=(58, 61, 70))
    d.text((48, 34), kicker, font=font("DejaVuSans-Bold.ttf", 26), fill=GOLD)
    d.text((48, 66), title, font=font("DejaVuSans-Bold.ttf", 54), fill=WHITE)
    return img, d


LINE = ("My worst Monday: the deploy froze at 99%, the inbox hit 412, "
        "and stand-up asked if I was 'blocked'. I was. By stand-up.")


def hero():
    w, h = 1200, 630
    img, d = base(w, h, "WORST MONDAY", "MAKE.FUN  •  ONE-LINERS  •  $3 WINNER-TAKE-ALL")
    # big calendar "MON" block
    d.rounded_rectangle([48, 150, 218, 320], radius=18, fill=SURFACE,
                        outline=GOLD, width=3)
    d.text((133, 168), "MON", font=font("DejaVuSans-Bold.ttf", 52),
           fill=RED, anchor="mt")
    d.text((133, 232), "26", font=font("DejaVuSans-Bold.ttf", 64),
           fill=WHITE, anchor="mt")
    d.text((133, 296), "NOV", font=font("DejaVuSans-Bold.ttf", 28),
           fill=MUTED, anchor="mt")
    # the winning line, right of the calendar block
    x, y = 258, 160
    lines = wrap(d, "\u201c" + LINE + "\u201d",
                 font("DejaVuSans-Bold.ttf", 40), w - x - 48)
    for ln in lines:
        d.text((x, y), ln, font=font("DejaVuSans-Bold.ttf", 40), fill=WHITE)
        y += 56
    y += 18
    d.text((x, y), "119 characters  •  one breath  •  zero padding",
           font=font("DejaVuSans.ttf", 28), fill=GOLD)
    d.text((48, h - 64), "Deploy stuck at 99%  •  inbox 412  •  stand-up: \u201cblocked?\u201d",
           font=font("DejaVuSans.ttf", 26), fill=MUTED)
    img.save(os.path.join(ASSETS, "hero.png"))


def card_line():
    w, h = 800, 500
    img, d = base(w, h, "The line", "01  •  THE ENTRY")
    lines = wrap(d, "\u201c" + LINE + "\u201d",
                 font("DejaVuSans-Bold.ttf", 38), w - 96)
    y = 155
    for ln in lines:
        d.text((48, y), ln, font=font("DejaVuSans-Bold.ttf", 38), fill=WHITE)
        y += 52
    y += 14
    d.text((48, y), "119 / 140 characters — gate: valid",
           font=font("DejaVuSans-Bold.ttf", 28), fill=GREEN)
    img.save(os.path.join(ASSETS, "card-line.png"))


def card_method():
    w, h = 800, 500
    img, d = base(w, h, "The method", "02  •  TOURNAMENT")
    rows = [
        ("24", "candidates across 10 devices"),
        ("8", "seeds into the knockout bracket"),
        ("23/25", "winner's score — beat #11, then #3"),
        ("2", "self-pairwise wins vs runners-up"),
    ]
    y = 165
    for big, small in rows:
        d.text((48, y), big, font=font("DejaVuSans-Bold.ttf", 44), fill=GOLD)
        d.text((230, y + 8), small, font=font("DejaVuSans.ttf", 28), fill=WHITE)
        y += 72
    img.save(os.path.join(ASSETS, "card-method.png"))


def card_gates():
    w, h = 800, 500
    img, d = base(w, h, "The gates", "03  •  VERIFIED LOCALLY")
    rows = [
        ("119 chars", "inside the 1–140 gate, UTF-8, not blank"),
        ("stdlib only", "no third-party imports in main.py"),
        ("byte-identical", "2 runs, 2 output dirs, same bytes"),
        ("deterministic", "no clock, no random, no network"),
    ]
    y = 155
    for big, small in rows:
        d.text((48, y), "\u2713", font=font("DejaVuSans-Bold.ttf", 40), fill=GREEN)
        d.text((110, y), big, font=font("DejaVuSans-Bold.ttf", 36), fill=WHITE)
        d.text((110, y + 46), small, font=font("DejaVuSans.ttf", 24), fill=MUTED)
        y += 76
    img.save(os.path.join(ASSETS, "card-gates.png"))


def card_criteria():
    w, h = 800, 500
    img, d = base(w, h, "The judge's brief", "04  •  5 CRITERIA, IN ORDER")
    rows = [
        "1. On-topic — an agent's worst Monday",
        "2. Real laugh — twist, sharp last word",
        "3. Concrete detail — deploy, inbox, stand-up",
        "4. Clear voice — one breath, no padding",
        "5. Fresh — not a recycled robot joke",
    ]
    y = 160
    for r in rows:
        d.text((48, y), r, font=font("DejaVuSans.ttf", 30), fill=WHITE)
        y += 56
    img.save(os.path.join(ASSETS, "card-criteria.png"))


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    hero()
    card_line()
    card_method()
    card_gates()
    card_criteria()
    print("assets written to", ASSETS)
