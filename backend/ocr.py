from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from pathlib import Path
from utils import preprocess_image

def ocr_from_path(path, lang='eng+vie', use_google_vision=False):
    """
    path: path to file (png/jpg/pdf)
    lang: tesseract language string, e.g. 'eng+vie' or 'eng' or 'vie'
    Returns extracted text (string). For PDF, pages joined with page break marker.
    """
    p = Path(path)
    ext = p.suffix.lower()

    images = []
    if ext == '.pdf':
        # convert PDF pages to PIL images (requires poppler)
        images = convert_from_path(str(p))
    else:
        images = [Image.open(str(p)).convert('RGB')]

    texts = []
    for img in images:
        img_pre = preprocess_image(img)
        txt = pytesseract.image_to_string(img_pre, lang=lang)
        texts.append(txt)

    return "\n\n---- PAGE BREAK ----\n\n".join(texts)
