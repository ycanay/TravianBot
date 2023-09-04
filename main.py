import pytesseract as tes
import cv2 as cv
import Detect_villa as dv
import Detect_time as dt
import Detect_edge as de

res_boundaries = {'x_min':657, 'x_max':1033, 'y_min':644, 'y_max':685}
city_boundaries = {'x_min':657, 'x_max':1033, 'y_min':745, 'y_max':786}

tes.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_no = 0

con1 = None
con2 = None
time_left_1 = None
time_left_2 = None

images = ['EU9_1_City.png', 'EU9_Res.png', 'INT2_2_City.png', 'INT2_2_Const.png', 'INT2_RES.png']

is_city = {
    'EU9_1_City.png': 1,
    'EU9_Res.png': 0,
    'INT2_2_City.png': 1,
    'INT2_2_Const.png': 0,
    'INT2_RES.png': 0
}

img = cv.imread('Image_Samples/' + images[image_no])
city = is_city[images[image_no]]

if not city:
    con1 = img[res_boundaries['y_min']:663, res_boundaries['x_min']:888]
    con1 = cv.cvtColor(con1, cv.COLOR_BGR2GRAY)
    con2 = img[663:res_boundaries['y_max'], res_boundaries['x_min']:888]
    con2 = cv.cvtColor(con2, cv.COLOR_BGR2GRAY)

    time_left_1 = img[res_boundaries['y_min']:663, 888:res_boundaries['x_max']]
    time_left_1 = cv.cvtColor(time_left_1, cv.COLOR_BGR2GRAY)

    time_left_2 = img[663:res_boundaries['y_max'], 888:res_boundaries['x_max']]
    time_left_2 = cv.cvtColor(time_left_2, cv.COLOR_BGR2GRAY)

else:
    con1 = img[city_boundaries['y_min']:764, city_boundaries['x_min']:888]
    con1 = cv.cvtColor(con1, cv.COLOR_BGR2GRAY)
    con2 = img[764:city_boundaries['y_max'], city_boundaries['x_min']:888]
    con2 = cv.cvtColor(con2, cv.COLOR_BGR2GRAY)

    time_left_1 = img[city_boundaries['y_min']:764, 888:city_boundaries['x_max']]
    time_left_1 = cv.cvtColor(time_left_1, cv.COLOR_BGR2GRAY)

    time_left_2 = img[764:city_boundaries['y_max'], 888:city_boundaries['x_max']]
    time_left_2 = cv.cvtColor(time_left_2, cv.COLOR_BGR2GRAY)

print(de.detect_edge(img))

print(dt.get_time_left(time_left_1))
print(dt.get_time(img))

cv.imshow("time_left", con1)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("time_left", con2)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("time_left", time_left_1)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imshow("time_left", time_left_2)
cv.waitKey(0)
cv.destroyAllWindows()
