#!/usr/bin/env bash
# Regenerate docs/pytest-ci-demo.gif
#
# Requirements:
#   pip install asciinema          # recorder
#   cargo install agg              # GIF renderer (no Chrome needed)
#
# Usage:
#   bash docs/demo.tape
#
# Previously used VHS (vhs docs/demo.tape), which requires a Chrome sandbox
# unavailable in headless CI. asciinema + agg are fully headless alternatives.

set -euo pipefail

CAST=$(mktemp /tmp/pytest-demo-XXXXXX.cast)
trap 'rm -f "$CAST"' EXIT

echo "Recording pytest run..."
asciinema rec \
  --overwrite \
  --cols 110 \
  --rows 32 \
  -c "python3 -m pytest automation/ -m 'not appium and not selenium and not slow' --tb=no -q" \
  "$CAST"

echo "Rendering GIF..."
agg \
  --theme dracula \
  --font-size 13 \
  --speed 10 \
  --idle-time-limit 1 \
  "$CAST" \
  docs/pytest-ci-demo.gif

echo "Done → docs/pytest-ci-demo.gif"
