#tiền xử lý ảnh cơ bản
from PIL import Image, ImageFilter, ImageOps

def preprocess_image(img: Image.Image) -> Image.Image:
    """
    Basic preprocessing: grayscale, autocontrast, resize (if too wide), sharpen.
    Bạn có thể mở rộng (deskew, denoise, adaptive threshold) để tăng accuracy.
    """
    # convert to grayscale
    img = img.convert('L')

    # resize if very large to avoid huge memory usage
    max_w = 2000
    if img.width > max_w:
        ratio = max_w / img.width
        new_h = int(img.height * ratio)
        img = img.resize((max_w, new_h))

    # auto contrast
    img = ImageOps.autocontrast(img)

    # sharpen
    img = img.filter(ImageFilter.SHARPEN)

    return img
