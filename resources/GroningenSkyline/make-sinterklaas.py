#!/usr/bin/env python3
"""Generate the Sinterklaas variant of the hero skyline.

Adds Sinterklaas on his horse riding back and forth over the gables of the
houses in front of the Martinitoren, and Pieten spread over the rooftops of
the whole skyline.

The ride (x 3984-4192) is the only roof stretch that stays visible and clear
of the hero buttons on every screen width from 360px phones to wide desktops. The animation uses SMIL, so it also runs when the SVG is used as
a CSS background image and scales exactly with the skyline.

Usage: python3 make-sinterklaas.py <in.svg> <out.svg> [day|night]
"""
import sys

COLOUR = {'day': '#071F55', 'night': '#03081A'}

# Hoof path over the two stepped gables between the Stadhuis and the Gasunie
RIDE_PATH = ('M3088 843 H3093 L3099 825 H3108 L3114 807 H3122 L3128 825 H3137 L3143 843 '
             'H3152 L3158 859 H3169 L3175 841 H3186 L3192 823 H3201 L3207 841 H3218 L3224 859 H3232')
RIDE_SECONDS = 36

# Silhouette facing right, feet at (0, 0)
SINT_ON_HORSE = '''
<path d="M-30 -42 Q-40 -38 -40 -20 Q-34 -30 -28 -34 Z"/>
<ellipse cx="0" cy="-38" rx="30" ry="12"/>
<path d="M18 -46 L32 -72 L40 -76 L54 -62 L51 -57 L38 -62 L30 -40 Z"/>
<path d="M36 -75 L38 -82 L41 -75 Z"/>
<rect x="-26" y="-32" width="5" height="32" rx="2"/>
<rect x="-17" y="-32" width="5" height="30" rx="2" transform="rotate(8 -15 -32)"/>
<rect x="13" y="-32" width="5" height="32" rx="2"/>
<rect x="21" y="-32" width="5" height="30" rx="2" transform="rotate(-8 23 -32)"/>
<path d="M-12 -44 L10 -44 L7 -78 L-7 -78 Z"/>
<path d="M-16 -46 Q-20 -60 -9 -76 L-6 -60 Z"/>
<circle cx="0" cy="-83" r="6"/>
<path d="M-4 -82 L8 -82 L4 -70 Z"/>
<path d="M-6 -88 L6 -88 L5 -100 L0 -108 L-5 -100 Z"/>
<rect x="15" y="-114" width="2.5" height="76"/>
<path d="M16 -114 Q16 -124 24 -122 Q29 -118 24 -114 Q21 -117 19 -114 Z"/>
<path d="M7 -70 L16 -66 L15 -62 L6 -64 Z"/>
'''

# Piet sitting on a roof ridge, seat at (0, 0)
PIET_SITTING = '''
<path d="M-7 0 L7 0 L5 -24 L-5 -24 Z"/>
<path d="M-6 -2 L-16 4 L-14 16 L-10 16 L-11 7 L-2 2 Z"/>
<path d="M6 -2 L13 6 L12 17 L8 17 L8 8 L1 2 Z"/>
<circle cx="0" cy="-29" r="5"/>
<path d="M-7 -32 Q0 -40 7 -32 Z"/>
<path d="M4 -37 Q10 -46 16 -42 Q10 -40 6 -35 Z"/>
<path d="M5 -20 L14 -26 L16 -23 L7 -17 Z"/>
'''

# Piet sitting with the sack of presents
PIET_WITH_SACK = PIET_SITTING + '''
<path d="M-12 -2 Q-24 -2 -24 -14 Q-24 -24 -15 -26 L-12 -30 L-9 -26 Q-4 -22 -5 -12 Z"/>
'''

# Piet standing on a roof, waving with both arms, feet at (0, 0)
PIET_WAVING = '''
<path d="M-6 -16 L6 -16 L5 -38 L-5 -38 Z"/>
<path d="M-6 -17 L-7 0 L-2 0 L0 -12 L2 0 L7 0 L6 -17 Z"/>
<path d="M-4 -36 L-14 -54 L-11 -56 L-1 -38 Z"/>
<path d="M4 -36 L14 -54 L11 -56 L1 -38 Z"/>
<circle cx="0" cy="-43" r="5"/>
<path d="M-7 -46 Q0 -54 7 -46 Z"/>
<path d="M4 -51 Q10 -60 16 -56 Q10 -54 6 -49 Z"/>
'''

# (pose, x, y, mirrored): seat/feet positions on roof tops, left to right
PIETEN = [
    (PIET_WAVING, 40, 830, False),
    (PIET_SITTING, 505, 806, True),
    (PIET_WITH_SACK, 2220, 823, False),
    (PIET_SITTING, 2345, 802, False),
    (PIET_WAVING, 2761, 798, True),
    (PIET_WAVING, 3985, 799, True),
    (PIET_WITH_SACK, 4594, 793, False),
    (PIET_WAVING, 4752, 778, False),
    (PIET_SITTING, 4924, 818, True),
    (PIET_WITH_SACK, 5096, 827, True),
]


def main(src, dst, mode):
    svg = open(src, encoding='utf-8').read()
    fill = COLOUR[mode]
    pieten = '\n'.join(
        '<g transform="translate({} {}){}">{}</g>'.format(x, y, ' scale(-1 1)' if mirrored else '', pose)
        for pose, x, y, mirrored in PIETEN)
    group = f'''<g id="sinterklaas" fill="{fill}">
<g>
<animateMotion dur="{RIDE_SECONDS}s" repeatCount="indefinite" calcMode="linear"
  path="{RIDE_PATH}" keyPoints="0;0;1;1;0;0" keyTimes="0;0.05;0.45;0.55;0.95;1"/>
<g>
<animateTransform attributeName="transform" type="scale" dur="{RIDE_SECONDS}s" repeatCount="indefinite"
  calcMode="discrete" values="1 1;-1 1" keyTimes="0;0.5"/>
<g>
<animateTransform attributeName="transform" type="translate" dur="0.9s" repeatCount="indefinite"
  values="0 0;0 -2.5;0 0"/>
{SINT_ON_HORSE}</g>
</g>
</g>
{pieten}
</g>
'''
    # Directly after the front houses, so he rides on top of their roofs
    anchor = svg.index('<g id="dot"')
    svg = svg[:anchor] + group + svg[anchor:]
    open(dst, 'w', encoding='utf-8').write(svg)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'day')
