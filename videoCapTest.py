import cv2 as cv
import numpy as np

#video capture obj
cap = cv.VideoCapture(0)

if (cap.isOpened() == False): 
  print("Unable to read camera feed")
  
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

while(True):
  ret, frame = cap.read()
 
  if ret == True: 
     
    # Write the frame into the file 'output.avi'
    #out.write(frame)
 
    # Display the resulting frame    
    cv.imshow('frame',frame)
 
    # Press Q on keyboard to stop recording
    if cv.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 

cap.release()
cv.destroyAllWindo()