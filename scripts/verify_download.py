"""Verify UpperMyo v1.0 data files; requires only Python 3."""
from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parents[1]
expected = {}
for line in (root / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
    digest, name = line.split("  ", 1)
    expected[name] = digest
errors = []
for i, (name, digest) in enumerate(expected.items(), 1):
    path = root / name
    if not path.is_file():
        errors.append("Missing: " + name)
        continue
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    if h.hexdigest() != digest:
        errors.append("Checksum mismatch: " + name)
actual = {p.relative_to(root).as_posix() for p in (root / "六通道数据集").rglob("*") if p.is_file()}
errors.extend("Unexpected data file: " + name for name in sorted(actual - expected.keys()))
for error in errors:
    print(error)
print(f"Verified {len(expected)} data files; {len(errors)} error(s).")
sys.exit(1 if errors else 0)
