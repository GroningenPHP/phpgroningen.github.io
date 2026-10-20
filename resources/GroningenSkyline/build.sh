#!/usr/bin/env bash
# Rebuild the website skyline images from the editable source.
# See SKYLINE-MANIFEST.md for details.
set -euo pipefail

cd "$(dirname "$0")"
SOURCE=groningenphp-skyline-hero.svg
OUT=../../public/images
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

python3 make-night.py "$SOURCE" "$TMP/night.svg"
python3 make-christmas.py "$SOURCE" "$TMP/christmas.svg" day
python3 make-christmas.py "$TMP/night.svg" "$TMP/christmas-night.svg" night
python3 make-christmas.py "$SOURCE" "$TMP/newyear.svg" day trees-only
python3 make-christmas.py "$TMP/night.svg" "$TMP/newyear-night.svg" night trees-only
python3 make-sinterklaas.py "$SOURCE" "$TMP/sinterklaas.svg" day
python3 make-sinterklaas.py "$TMP/night.svg" "$TMP/sinterklaas-night.svg" night

svgo() { npx --yes svgo@3 --config svgo.config.cjs -q "$1" -o "$2"; }
svgo "$SOURCE" "$OUT/groningenphp-skyline.svg"
svgo "$TMP/night.svg" "$OUT/groningenphp-skyline-night.svg"
svgo "$TMP/christmas.svg" "$OUT/groningenphp-skyline-christmas.svg"
svgo "$TMP/christmas-night.svg" "$OUT/groningenphp-skyline-christmas-night.svg"
svgo "$TMP/newyear.svg" "$OUT/groningenphp-skyline-newyear.svg"
svgo "$TMP/newyear-night.svg" "$OUT/groningenphp-skyline-newyear-night.svg"
svgo "$TMP/sinterklaas.svg" "$OUT/groningenphp-skyline-sinterklaas.svg"
svgo "$TMP/sinterklaas-night.svg" "$OUT/groningenphp-skyline-sinterklaas-night.svg"

ls -la "$OUT"/groningenphp-skyline*.svg
