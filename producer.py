import numpy as np
import cv2
import redis
import asyncio
import threading
import base64
import pickle
r = redis.Redis(
    host='192.168.1.112',
    port=6379
)
cap = cv2.VideoCapture(0)


def asynctask(s):
    r.publish("frame", pickle.dumps(s))


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        t = threading.Thread(target=asynctask, args=[frame], daemon=True)
        t.start()

        frame = cv2.flip(cv2.flip(frame, -1), 0)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
