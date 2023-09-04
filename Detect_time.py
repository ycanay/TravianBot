import cv2 as cv
import pytesseract as tes
import time

tes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_time(img):
    roi = img[80:95, 250:400]
    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    written = tes.image_to_string(roi)
    written = written.upper()
    written = written.split(': ')[1]
    written = written.strip()
    time_obj = time.strptime(written, '%H:%M:%S')
    return time_obj

def get_time_left(img):
    written = tes.image_to_string(img)
    done = written.split('at')[1].strip()
    done_time = time.strptime(done, '%H:%M')
    left = written.split('hrs')[0].strip()
    left_time = time.strptime(left, '%H:%M:%S')

    return left_time
