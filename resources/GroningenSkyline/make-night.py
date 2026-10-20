#!/usr/bin/env python3
"""Generate the night variant of the hero skyline.

Darkens every colour towards a night blue and lights up a (deterministic)
selection of the small window rectangles with a warm glow.

Usage: python3 make-night.py <day.svg> <night.svg>
Afterwards compress both files (keeps the viewBox):
    npx svgo --config svgo.config.cjs <in.svg> -o <out.svg>
"""
import random
import re
import sys

NIGHT = (11, 21, 48)          # colour everything is blended towards
DARKEN = 0.55                 # 0 = unchanged, 1 = fully night blue
WINDOW_COLOURS = {'#3E68C0', '#3A4F7A'}
LIT_COLOURS = ['#FFD27A', '#FFC65C', '#FFE3A3']
LIT_RATIO = 0.6
MAX_WINDOW_SIZE = (40, 60)    # width, height


def darken(hex_colour):
    h = hex_colour.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    mix = lambda c, n: round(c + (n - c) * DARKEN)
    return '#{:02X}{:02X}{:02X}'.format(mix(r, NIGHT[0]), mix(g, NIGHT[1]), mix(b, NIGHT[2]))


def main(src, dst):
    svg = open(src, encoding='utf-8').read()
    rng = random.Random(42)

    def light_window(match):
        tag = match.group(0)
        fill = re.search(r'fill="(#[0-9A-Fa-f]{6})"', tag)
        width = re.search(r'width="([\d.]+)"', tag)
        height = re.search(r'height="([\d.]+)"', tag)
        if (fill and width and height
                and fill.group(1).upper() in WINDOW_COLOURS
                and float(width.group(1)) <= MAX_WINDOW_SIZE[0]
                and float(height.group(1)) <= MAX_WINDOW_SIZE[1]
                and rng.random() < LIT_RATIO):
            # Mark as lit so the darkening pass below skips it
            return tag.replace(fill.group(0), 'fill="LIT{}"'.format(rng.choice(LIT_COLOURS)))
        return tag

    svg = re.sub(r'<rect\b[^>]*/>', light_window, svg)
    svg = re.sub(r'(fill|stop-color|stroke)="(#[0-9A-Fa-f]{3,6})"',
                 lambda m: '{}="{}"'.format(m.group(1), darken(m.group(2))), svg)
    svg = svg.replace('fill="LIT', 'fill="')
    open(dst, 'w', encoding='utf-8').write(svg)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
