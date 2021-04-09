import cv2
import sys


cv2.namedWindow('image')
cv2.moveWindow('image', 250, 150)

video = sys.argv[1]
cap = cv2.VideoCapture(video)

frame_rate = 24

state=1
while True:
    if state:
        ret, im = cap.read()
        if ret:
            # boyutlandırma
            r = 750.0 / im.shape[1]
            dim = (750, int(im.shape[0] * r))
            im = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)
            if im.shape[0] > 600:
                im = cv2.resize(im, (500, 500))
                controls = cv2.resize(controls, (im.shape[1], 25))
            # boyutlandırma
        else:
            print("program bitti")
            break
        cv2.imshow('image', im)
        
    cv2.waitKey(60//frame_rate)
        

cv2.destroyWindow('image')
