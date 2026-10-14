#!/usr/bin/env python3
"""Export slide images from a user-provided PDF for local LuaLaTeX build.
Usage: python scripts/extract_chapter1_slides.py 'Chapter 1_An overview of IoT.pdf'
"""
import sys
from pathlib import Path

try:
    import fitz
except ImportError as exc:
    raise SystemExit('Install PyMuPDF: python -m pip install pymupdf') from exc

if len(sys.argv) != 2:
    raise SystemExit('Usage: python scripts/extract_chapter1_slides.py path/to/chapter1_slides.pdf')

pdf_path = Path(sys.argv[1]).expanduser().resolve()
output = Path(__file__).resolve().parent.parent / 'assets' / 'chapter1'
output.mkdir(parents=True, exist_ok=True)
slides = fitz.open(pdf_path)
if len(slides) != 50:
    raise SystemExit(f'Expected 50 slides, found {len(slides)}. Check the source PDF.')
for number, page in enumerate(slides, start=1):
    pix = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False)
    from PIL import Image
    image = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
    image.save(output / f'slide{number:02d}.jpg', quality=82, optimize=True)
print(f'Exported {len(slides)} slides to {output}')