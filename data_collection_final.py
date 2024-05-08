import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import os
import traceback

capture = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)
hd2 = HandDetector(maxHands=1)

count = len(os.listdir("AtoZ_3.1"))
c_dir = 'A'

offset = 15
step = 1
flag = False
suv = 0

white = np.ones((400, 400), np.uint8) * 255
cv2.imwrite("./white.jpg", white)

while True:
    try:
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)
        hands = hd.findHands(frame, draw=False, flipType=True)

        if hands and len(hands) > 0:
            hand = hands[0]
            if 'bbox' in hand:
                bbox = hand['bbox']
                x, y, w, h = bbox
            else:
                # Handle case where 'bbox' key is not present in the hand dictionary
                continue  # Skip the rest of the loop iteration if no bounding box is found
        else:
            # Handle case where no hands are detected
            continue  # Skip the rest of the loop iteration if no hands are found

        white = cv2.imread("./white.jpg")

        image = np.array(frame[y - offset:y + h + offset, x - offset:x + w + offset])

        handz, imz = hd2.findHands(image, draw=True, flipType=True)
        if handz:
            hand = handz[0]
            pts = hand['lmList']
            os = ((400 - w) // 2) - 15
            os1 = ((400 - h) // 2) - 15
            for t in range(0, 4, 1):
                cv2.line(white, (pts[t][0] + os, pts[t][1] + os1), (pts[t + 1][0] + os, pts[t + 1][1] + os1),
                         (0, 255, 0), 3)

        frame = cv2.putText(frame, "dir=" + str(c_dir) + "  count=" + str(count), (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow("frame", frame)
        interrupt = cv2.waitKey(1)
        if interrupt & 0xFF == 27:
            # esc key
            break

    except Exception:
        print("==", traceback.format_exc())

capture.release()
cv2.destroyAllWindows()