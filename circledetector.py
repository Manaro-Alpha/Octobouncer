import numpy as np
import cv2
import time

vid = cv2.VideoCapture('http://10.20.141:4747/')
def poly(x):
    pol = (-4.46*(10**-6))*(x**4) + (1.5*(10**-3))*(x**3) + (-0.183)*(x**2) + 9.26*x - 129.5
    return pol
'''
while(True):
        
        # Capture the video frame
        # by frame
    ret, frame = vid.read()

        # Display the resulting frame
    cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # After the loop release the cap object
vid.release()
    # Destroy all the windows
cv2.destroyAllWindows()

#def circle_detect(img,)'''
while(True):
    ret,img = vid.read()
    cv2.imshow('img',img)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgGrayBlur = cv2.blur(imgGray,(3,3))
    detected_circles = cv2.HoughCircles(imgGrayBlur,cv2.HOUGH_GRADIENT_ALT, 1, 20, param1 = 300,param2 = 0.9, minRadius = 30, maxRadius = 500)
    #cv2.imshow('circle',img)

    #detected_circles = np.uint16(np.around(detected_circles))
    #if detected_circles is not None:
        
        #circle = detected_circles.copy()
        #circles = np.round(detected_circles[0, :]).astype("int")
    for circles in detected_circles:
            #cv2.circle(img, (x,y), r, (36,255,12), 3)
  
        # Draw the circumference of the circle.
            #cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
            #cv2.circle(img, (x, y), 1, (0, 0, 255), 3)
            #print(x,y,r)
            #print(r,poly(r))
            #cv2.imshow("Detected Circle", img)
        print(detected_circles[0][0][2],poly(detected_circles[0][0][2]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
    # Destroy all the windows
cv2.destroyAllWindows()