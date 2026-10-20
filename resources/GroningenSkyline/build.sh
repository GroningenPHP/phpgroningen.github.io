#!/usr/bin/env bash
# Rebuild the website skyline images from the editable source.
# See SKYLINE-MANIFEST.md for details.
set -euo pipefail

cd "$(dirname "$0")"
SOURCE=groningenphp-skyline-hero.svg
OUT=../../public/images
NIGHT_TMP=$(mktemp --suffix=.svg)
trap 'rm -f "$NIGHT_TMP"' EXIT

python3 make-night.py "$SOURCE" "$NIGHT_TMP"
npx --yes svgo@3 --config svgo.config.cjs -q "$SOURCE" -o "$OUT/groningenphp-skyline.svg"
npx --yes svgo@3 --config svgo.config.cjs -q "$NIGHT_TMP" -o "$OUT/groningenphp-skyline-night.svg"

ls -la "$OUT"/groningenphp-skyline*.svg
