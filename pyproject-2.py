import numpy as np
import cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        newImg = np.zeros((250,250,3), np.uint8)
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        newImg[:] = [blue, green, red]
        images.append(newImg)
        imgName = 'color#' + str(len(images))
        font = cv.FONT_HERSHEY_SIMPLEX
        rgb = 'R: ' + str(red) + ' G:' + str(green) + ' B:' + str(blue)
        cv.putText(newImg, rgb, (15,15), font, .5, (255,255,255), 2)
        cv.imshow(imgName, newImg)

def nothing(x):
    print(x)

images = []

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', click_event)

cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

switch = '1 : ON\n 0: OFF'
cv.createTrackbar(switch, 'image', 1, 0, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G','image')
    r = cv.getTrackbarPos('R','image')
    s = cv.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()