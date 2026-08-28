from pathlib import Path

import pytesseract
from PIL import Image


def extract_text(image_path: str) -> str:
    """Extract text from an image using Tesseract OCR."""
    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(f"Image not found: {path}")

    return pytesseract.image_to_string(Image.open(path)).strip()
