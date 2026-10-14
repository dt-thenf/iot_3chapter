#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/build_chapter2.py
for pass in 1 2 3; do
  echo "LuaLaTeX combined, pass $pass/3"
  lualatex -interaction=nonstopmode -halt-on-error -file-line-error -jobname=iot_3_chuong main.tex > combined-build.log 2>&1 || { tail -n 120 combined-build.log; exit 1; }
done
for pass in 1 2; do
  echo "LuaLaTeX six questions, pass $pass/2"
  lualatex -interaction=nonstopmode -halt-on-error -file-line-error on_tap_tu_luan_6_cau.tex > six-questions-build.log 2>&1 || { tail -n 120 six-questions-build.log; exit 1; }
done
test -s iot_3_chuong.pdf
test -s on_tap_tu_luan_6_cau.pdf
echo "OK: iot_3_chuong.pdf and on_tap_tu_luan_6_cau.pdf"
