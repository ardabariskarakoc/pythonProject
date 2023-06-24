import cv2

cap =cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('Camera',frame)
    q = cv2.waitKey(1)
    if q== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
