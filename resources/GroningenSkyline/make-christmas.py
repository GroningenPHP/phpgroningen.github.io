#!/usr/bin/env python3
"""Generate the Christmas variant of the hero skyline.

Every December the round trees become decorated fir trees, a big Christmas
tree stands in front of the Stadhuis and the DOT dome is dressed up as a giant green Christmas bauble
with strings of lights and a hanger on top. This script restyles the
`<g id="dot">` group of an unoptimised skyline SVG (day source or the raw
output of make-night.py) accordingly.

Usage: python3 make-christmas.py <in.svg> <out.svg> [day|night] [trees-only]

`trees-only` keeps the plain DOT (used for the New Year images).
"""
import math
import re
import sys

# Big decorated tree in front of the right wing of the Stadhuis
BIG_TREE_X, BIG_TREE_SCALE = 2675, 2.0
GROUND = 962

# Dome centre and radius inside the dot group (before its transform)
CX, CY, R = 3730, 787, 145
TOP = CY - R

PALETTE = {
    'day': {
        'green': ('#5FD47F', '#1E9B4A', '#0E6A30'),
        'lights': ['#FFFFFF', '#C9A2FF', '#FF8CC6', '#9EC9FF'],
        'cap': '#E8EEF8',
        'glow': None,
        'baubles': ['#E5243B', '#F2B705', '#FFFFFF', '#3E7BFA'],
        'star': '#F2B705',
    },
    'night': {
        'green': ('#5CFF8A', '#1FBF55', '#0B7A33'),
        'lights': ['#FFFFFF', '#C58CFF', '#FF6FB5', '#8FC2FF'],
        'cap': '#FFFFFF',
        'glow': '#3CE66E',
        'baubles': ['#FF4D5E', '#FFD54A', '#FFFFFF', '#7FB0FF'],
        'star': '#FFE27A',
    },
}


def light_string(shape, colour):
    return ('{} fill="none" stroke="{}" stroke-width="6" stroke-linecap="round" '
            'stroke-dasharray="0 12"/>'.format(shape, colour))


# Round deciduous trees of the master: trunk rect plus three circles
TREE_RE = re.compile(
    r'<g fill="(?P<leaf>#[0-9A-Fa-f]{6})">\s*'
    r'<rect fill="(?P<trunk>#[0-9A-Fa-f]{6})" height="58" width="8" x="[\d.]+" y="904"/>\s*'
    r'<circle cx="(?P<cx>[\d.]+)" cy="900" r="(?P<r>[\d.]+)"/>\s*'
    r'(?:<circle [^>]*/>\s*){2}</g>')

# Fir tree, ground at (0, 0), about 76 wide and 104 tall
TIERS = ['M-38 -20 Q0 -12 38 -20 L0 -62 Z', 'M-30 -46 Q0 -39 30 -46 L0 -84 Z', 'M-21 -70 Q0 -64 21 -70 L0 -104 Z']
BAUBLES = [(-24, -22), (14, -21), (-6, -36), (24, -30), (-15, -50), (10, -52), (-3, -70), (12, -74), (-9, -88)]


def star(cx, cy, r, fill):
    pts = []
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append('{:.1f},{:.1f}'.format(cx + rr * math.cos(a), cy - rr * math.sin(a)))
    return '<polygon points="{}" fill="{}"/>'.format(' '.join(pts), fill)


def fir_tree(x, scale, leaf, trunk, p, big=False):
    parts = ['<rect x="-4" y="-24" width="8" height="24" fill="{}"/>'.format(trunk)]
    parts += ['<path d="{}"/>'.format(d) for d in TIERS]
    # Shade the right half of each tier
    parts += ['<path d="{}" fill="#000" opacity="0.18" clip-path="url(#fir-right)"/>'.format(d) for d in TIERS]
    if big:
        parts.append(light_string('<path d="M-30 -26 Q0 -16 26 -36 M-22 -52 Q0 -42 20 -62 M-14 -76 Q0 -70 12 -86"',
                                  p['lights'][0]).replace('stroke-width="6"', 'stroke-width="3"')
                     .replace('0 12', '0 6'))
        baubles = BAUBLES
    else:
        baubles = BAUBLES[::2]
    for i, (bx, by) in enumerate(baubles):
        parts.append('<circle cx="{}" cy="{}" r="{}" fill="{}"/>'.format(
            bx, by, 3.2 if big else 4, p['baubles'][i % len(p['baubles'])]))
    parts.append(star(0, -106, 9 if big else 7, p['star']))
    if big and p['glow']:
        parts.insert(0, '<ellipse cx="0" cy="-60" rx="60" ry="70" fill="url(#tree-glow)"/>')
    return '<g fill="{}" transform="translate({} {}) scale({})">{}</g>'.format(
        leaf, x, GROUND, scale, ''.join(parts))


def dress_dot(svg, p):
    start = svg.index('<g id="dot"')
    end = svg.index('</g>', start)
    group = svg[start:end]

    # Drop the grey lattice lines of the normal dome
    group = re.sub(r'\s*<ellipse\b[^>]*fill="none"[^>]*/>', '', group)
    group = re.sub(r'\s*<line\b[^>]*/>', '', group)

    dome = re.search(r'<circle\b[^>]*url\(#dome\)[^>]*/>', group).group(0)
    lights = p['lights']
    decorations = [
        '<circle cx="{}" cy="{}" r="{}" fill="url(#ornament)"/>'.format(CX, CY, R),
        # Meridians of the bauble, from the outer edge towards the centre
        light_string('<circle cx="{}" cy="{}" r="{}"'.format(CX, CY, R - 2), lights[2]),
        light_string('<ellipse cx="{}" cy="{}" rx="105" ry="{}"'.format(CX, CY, R), lights[1]),
        light_string('<ellipse cx="{}" cy="{}" rx="50" ry="{}"'.format(CX, CY, R), lights[0]),
        light_string('<line x1="{0}" y1="{1}" x2="{0}" y2="{2}"'.format(CX, TOP + 4, CY + R), lights[3]),
    ]
    if p['glow']:
        decorations.insert(0, '<circle cx="{}" cy="{}" r="{}" fill="url(#ornament-glow)"/>'.format(CX, CY, R + 28))
    group = group.replace(dome, '\n'.join(decorations))

    # Hanger: a little lattice cap with a loop of lights on top
    cap = [
        '<rect x="{}" y="{}" width="44" height="22" rx="3" fill="{}" opacity="0.9"/>'.format(CX - 22, TOP - 18, p['cap']),
        '<path d="M{0} {1}v22M{2} {1}v22M{3} {1}v22M{4} {5}h44" stroke="#7A8AA8" stroke-width="2"/>'.format(
            CX - 11, TOP - 18, CX, CX + 11, CX - 22, TOP - 7),
        light_string('<path d="M{} {} C{} {} {} {} {} {}"'.format(
            CX - 16, TOP - 18, CX - 22, TOP - 70, CX + 22, TOP - 70, CX + 16, TOP - 18), lights[0]),
    ]
    group += '\n' + '\n'.join(cap) + '\n'
    svg = svg[:start] + group + svg[end:]
    return svg


def main(src, dst, mode, trees_only=False):
    p = PALETTE[mode]
    svg = open(src, encoding='utf-8').read()

    if not trees_only:
        svg = dress_dot(svg, p)

    # Swap the round trees for fir trees and add a big one by the Stadhuis
    trees = list(TREE_RE.finditer(svg))
    if not trees:
        raise SystemExit('no trees found')
    leaf, trunk = trees[0].group('leaf'), trees[0].group('trunk')
    for m in reversed(trees):
        scale = float(m.group('r')) / 31
        svg = svg[:m.start()] + fir_tree(float(m.group('cx')), scale, leaf, trunk, p) + svg[m.end():]
    anchor = svg.index('<g id="dot"')
    anchor = svg.rindex('</g>', 0, anchor)  # end of the front layer
    svg = svg[:anchor] + fir_tree(BIG_TREE_X, BIG_TREE_SCALE, leaf, trunk, p, big=True) + '\n' + svg[anchor:]

    defs = ''
    if not trees_only:
        green = p['green']
        defs += (
            '<radialGradient id="ornament" cx="0.38" cy="0.32" r="0.75">'
            '<stop offset="0" stop-color="{}"/><stop offset="0.55" stop-color="{}"/>'
            '<stop offset="1" stop-color="{}"/></radialGradient>'.format(*green)
        )
        if p['glow']:
            defs += (
                '<radialGradient id="ornament-glow"><stop offset="0.6" stop-color="{0}" stop-opacity="0.28"/>'
                '<stop offset="1" stop-color="{0}" stop-opacity="0"/></radialGradient>'.format(p['glow'])
            )
    defs += '<clipPath id="fir-right"><rect x="0" y="-120" width="60" height="120"/></clipPath>'
    if p['glow']:
        defs += ('<radialGradient id="tree-glow"><stop offset="0" stop-color="#FFD54A" stop-opacity="0.35"/>'
                 '<stop offset="1" stop-color="#FFD54A" stop-opacity="0"/></radialGradient>')
    svg = svg.replace('<defs>', '<defs>' + defs, 1)
    open(dst, 'w', encoding='utf-8').write(svg)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'day',
         len(sys.argv) > 4 and sys.argv[4] == 'trees-only')
