#!/usr/bin/env bash
# Runs the Appium smoke suite against the local Android emulator started by
# reactivecircus/android-emulator-runner in .github/workflows/ci.yml.
#
# This exists as a standalone, testable file (bash -n / shellcheck) rather
# than an inline `script: |` block in the workflow YAML — the previous
# attempt (2026-07-09) hit a shell syntax error inside that inline block
# which left the emulator-runner action's shutdown routine hanging for the
# full 6h job timeout instead of failing fast. See docs/QA_AUDIT.md §3.7.
set -euo pipefail

appium --log appium.log &

appium_ready=""
for _ in $(seq 1 30); do
  if curl -sf http://127.0.0.1:4723/status > /dev/null; then
    appium_ready=1
    break
  fi
  sleep 2
done

if [ -z "$appium_ready" ]; then
  echo "Appium server did not become ready within 60s" >&2
  exit 1
fi

mkdir -p test-results

pytest automation/tests/appium/ \
  -m "appium" \
  --html=test-results/appium-report.html \
  --self-contained-html \
  --junitxml=test-results/appium-results.xml \
  --reruns 1 --reruns-delay 5 \
  -s -v
