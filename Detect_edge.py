import cv2 as cv
import pytesseract as tes

tes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def is_edge(img):
    roi = img[122:134, 275:358]
    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    written = tes.image_to_string(roi).strip()
    if written == 'LEGENDS.':
        return True
    else:
        return False
