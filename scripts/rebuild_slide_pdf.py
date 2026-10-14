#!/usr/bin/env python3
"""Reconstruct the lecturer's slide PDF from tracked base64 parts.

This keeps the archive in GitHub's UTF-8 contents API without losing
figures, tables, plots or the original page layout.
"""
import base64
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIECES = ROOT / 'source' / 'base64'
DEST = ROOT / 'source' / 'chapter3-slides.pdf'
EXPECTED_SHA256 = '9647585a32a4e3052478dcba76c47f031f6bad36cfe9e4d9df06e7df9b41f0fe'


def main():
    paths = sorted(PIECES.glob('chapter3.part*.b64'))
    if len(paths) != 9:
        raise RuntimeError(f'Expected nine slide archive parts, received {len(paths)}')
    src = ''.join(''.join(f.read_text(encoding='ascii').split()) for f in paths)
    payload = base64.b64decode(src, validate=True)
    actual_sha = hashlib.sha256(payload).hexdigest()
    if actual_sha != EXPECTED_SHA256:
        raise RuntimeError(f'Slide checksum mismatch! SHA256={actual_sha}')
    if not payload.startswith(b'%PDF'):
        raise RuntimeError('Reconstructed file is not a PDF')
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_bytes(payload)
    print(f'Reconstructed {DEST} ({len(payload)} bytes); SHA256 validated.')


if __name__ == '__main__':
    main()