#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo PDF Chương 2 từ 12 tệp Base64 đã lưu trong repository.

Dùng:
  python scripts/build_chapter2.py
  python scripts/build_chapter2.py --compile

Không tải tài nguyên từ Internet, không can thiệp Chương 1/3.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_DIR = ROOT / "source" / "base64"
OUTPUT = ROOT / "assets" / "chapter2_original_slides.pdf"
EXPECTED_SHA256 = "2e741ee40a26785b1b6b64a50ba5630e29398e965625a9b03d8085ce9324de60"
EXPECTED_SIZE = 5_112_150
EXPECTED_PARTS = 12


def reconstruct_pdf() -> Path:
    parts = sorted(PART_DIR.glob("chapter2.part*.b64"))
    expected_names = [f"chapter2.part{i:02d}.b64" for i in range(1, EXPECTED_PARTS + 1)]
    names = [p.name for p in parts]
    if names != expected_names:
        raise RuntimeError(f"Thiếu hoặc sai thứ tự tệp Base64: {names}")
    text = "".join(p.read_text(encoding="ascii").strip() for p in parts)
    pdf_bytes = base64.b64decode(text, validate=True)
    sha256 = hashlib.sha256(pdf_bytes).hexdigest()
    if len(pdf_bytes) != EXPECTED_SIZE or sha256 != EXPECTED_SHA256:
        raise RuntimeError(
            f"Dữ liệu không khớp PDF nguồn: size={len(pdf_bytes)}, sha256={sha256}"
        )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(pdf_bytes)
    print(f"Đã khôi phục: {OUTPUT.relative_to(ROOT)}, {len(pdf_bytes):,} byte, SHA-256 OK")
    return OUTPUT


def compile_chapter() -> None:
    for number in (1, 2):
        print(f"LuaLaTeX lượt {number}/2...")
        subprocess.run(
            ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "chapter2_main.tex"],
            cwd=ROOT, check=True
        )
    print("Đã tạo chapter2_main.pdf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compile", action="store_true", help="Biên dịch PDF với LuaLaTeX")
    args = parser.parse_args()
    reconstruct_pdf()
    if args.compile:
        compile_chapter()
