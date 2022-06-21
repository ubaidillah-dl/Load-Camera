import cv2

cap=cv2.VideoCapture(0)

while True:
    _,camera=cap.read()
    
    cv2.imshow('Camera',camera)
    
    if cv2.waitKey(1)==ord('p'):
        break

camera.release()
cv2.destroyAllWindows()