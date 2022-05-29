"""
Imported libraries:
1. cv2 (OpenCV): For image/frame processing
2. Numpy: For functions related to array
3. Dlib: For face and landmark detections and for using deep learning modules (image processing)
4. face_utils: For detection and conversion operations
"""


import cv2
import numpy as np
import dlib
from imutils import face_utils

# To initialize the camera and start capturing frames
cap = cv2.VideoCapture(0)

# Initializing the face and landmark detector
# (Using dlib as it is more accurate than the haar cascade detector)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initializing variables
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

# Calculating the Euclidean distance between two points
def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist


def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    if ratio > 0.25:
        return 2
    elif 0.15 < ratio <= 0.25:
        return 1
    else:
        return 0


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    face_frame = frame.copy()
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        # face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        # Here the numbers are "eye landmarks-1" ('-1' as array starts with zero)
        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[47], landmarks[46], landmarks[45])

        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 6:
                status = "DON'T SLEEP !!"
                color = (255, 0, 0)

        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "WATCH OUT drowsy person !"
                color = (0, 0, 255)

        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 6:
                status = "All active and fresh :))"
                color = (0, 255, 0)

        cv2.putText(frame, status, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        for n in range(0, 68):
            (x, y) = landmarks[n]
            cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)

    cv2.imshow("Status", frame)
    cv2.imshow("Face landmarks", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
