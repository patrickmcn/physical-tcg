import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
frame_rate = 5
prev = 0
while True:
    time_elapsed = time.time() - prev
    ret, frame = cap.read()
    if time_elapsed > 1./frame_rate:
        prev = time.time()
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows