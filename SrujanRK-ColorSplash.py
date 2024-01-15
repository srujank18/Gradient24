import cv2
import numpy as np
print('Gradient Tech Team Recruitment - ColorSplash - Srujan R Kumar\n')

color_lower = np.array([0, 20, 70]) #Selecting the color range (below range suitable for skin color values)
color_higher = np.array([20, 255, 255])
print("Lower Color:", color_lower)
print("Upper Color:", color_higher) #printing lower and higher color range values 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #Capturing frames
    if not ret:
        print("Failed to capture frame.")
        continue
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converting BGR to HSV 

    mask = cv2.inRange(hsv, color_lower, color_higher) #Creating a mask to extract specified color
    cv2.imshow('Binary Mask Result', mask)

    result_bit = cv2.bitwise_and(frame, frame, mask=mask) #Bitwise AND (highlighting color in original frame)

    highlighted_cap = cv2.addWeighted(frame, 1.5, result_bit, 0.5, 0) #Combining Highlighted and original frames

    cv2.imshow('Highlighted Color - ColorSplash Cam - Gradient', highlighted_cap) #identified color popped on screen

    if cv2.waitKey(1) == 27: #Esc to break from loop 
        break
        
cap.release()
cv2.destroyAllWindows()
