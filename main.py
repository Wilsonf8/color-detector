import cv2
from PIL import Image
from util import get_limits


yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0)

def apply_blur(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)

while True:
    ret, frame = cap.read()
    blurred_frame = apply_blur(frame)

    hsvImage = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()