import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

USE_GOOGLE_VISION = os.getenv('USE_GOOGLE_VISION', 'false').lower() == 'true'
GOOGLE_CRED_PATH = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', '')

# path to tesseract if needed (Windows)
TESSERACT_CMD = os.getenv('TESSERACT_CMD', '')
if TESSERACT_CMD:
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
