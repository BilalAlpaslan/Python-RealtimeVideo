import cv2
import redis
import pickle
import time
import threading
import os

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc, 24, (640,480))

r =redis.StrictRedis(
    host='192.168.1.112',
    port=6379
)
p = r.pubsub()
p.subscribe("frame")


for i in p.listen():
    if i:
        if i["data"]!=1:
            frame=pickle.loads(i["data"])
            cv2.imshow('image', frame)
            # out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("program bitti")
        break 


