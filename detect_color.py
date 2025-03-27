# Detects color using camera. Limited to 5 frames per second

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
        
        # Converts color values from BGR (blue green red) to HSV (hue saturation value)
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Red color range and mask
        red_lower = np.array([136, 87, 111], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
        
        # Green color range and mask
        green_lower = np.array([25, 52, 72], np.uint8) 
        green_upper = np.array([102, 255, 255], np.uint8) 
        green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

        # Blue color range and mask
        blue_lower = np.array([94, 80, 2], np.uint8) 
        blue_upper = np.array([120, 255, 255], np.uint8) 
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 

        kernel = np.ones((5, 5), "uint8")

        # Dilates and masks red
        red_mask = cv2.dilate(red_mask, kernel)
        res_red = cv2.bitwise_and(frame, frame, mask = red_mask)

        # Dilates and masks green
        green_mask = cv2.dilate(green_mask, kernel)
        res_green = cv2.bitwise_and(frame, frame, mask = green_mask)

        # Dilates and masks blue
        blue_mask = cv2.dilate(blue_mask, kernel)
        res_blue = cv2.bitwise_and(frame, frame, mask = blue_mask)

        # Creates red contour
        contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 300:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, "RED", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

        # Creates green contour
        contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 300:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "GREEN", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

        # Creates blue contour
        contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if area > 300:
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, "BLUE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
        
        # Displays output
        cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows