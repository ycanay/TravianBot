import cv2 as cv
import pytesseract as tes

tes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def get_villas(img):
    no_village = get_villa_count(img)
    start_px = 430
    end_px = start_px + (no_village*21) + 10
    roi = img[start_px:end_px, 1380:1555]
    cv.imshow('roi', roi)
    cv.waitKey(0)
    cv.destroyAllWindows()
    names = tes.image_to_string(roi)
    names = names.split('\n')
    names = names[0:len(names)-1]
    for name in names:
        name = names.upper()
        print('villa name : ' + name)

    return roi


def get_villa_count(img):
    roi = img[387:409, 1390:1640]
    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    written = tes.image_to_string(roi)
    written = written.split(' ')[1].split('/')[0]
    written = int(written)
    return written

def get_villa_name(img):
    roi = img[263:285, 1393:1610]
    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    cv.imshow("time_left", roi)
    cv.waitKey(0)
    cv.destroyAllWindows()
    written = tes.image_to_string(roi)
    written = written.upper()
    print(written)
    return written


def detect_villa(img):
    get_villa_name(img)
