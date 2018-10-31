#!/usr/bin/env python

import numpy as np
import cv2


def captureCamera(left=False):
    cap = cv2.VideoCapture(0)

    outerRectangleXIni = 300
    outerRectangleYIni = 50
    outerRectangleXFin = 550
    outerRectangleYFin = 300
    innerRectangleXIni = 400
    innerRectangleYIni = 150
    innerRectangleXFin = 450
    innerRectangleYFin = 200

    if left:
        move_to_left = 250
        outerRectangleXIni = outerRectangleXIni - move_to_left
        outerRectangleXFin = outerRectangleXFin - move_to_left
        innerRectangleXIni = innerRectangleXIni - move_to_left
        innerRectangleXFin = innerRectangleXFin - move_to_left

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(frame, (outerRectangleXIni, outerRectangleYIni),
                      (outerRectangleXFin, outerRectangleYFin), (0, 255, 0), 0)
        cv2.rectangle(frame, (innerRectangleXIni, innerRectangleYIni),
                      (innerRectangleXFin, innerRectangleYFin), (255, 0, 0), 0)
        cv2.putText(frame, 'Please center your hand in the square', (0, 35),
                    font, 1, (255, 0, 0), 3, cv2.LINE_AA)
        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            cap.release()
            return None
        elif key != -1:
            roi = frame[innerRectangleYIni +
                        1:innerRectangleYFin, innerRectangleXIni +
                        1:innerRectangleXFin]
            display_result(roi)
            approved = wait_approval()
            if approved:
                break
            cv2.destroyAllWindows()

    cap.release()
    hsvRoi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    lower = np.array(
        [hsvRoi[:, :, 0].min(), hsvRoi[:, :, 1].min(), hsvRoi[:, :, 2].min()])
    upper = np.array(
        [hsvRoi[:, :, 0].max(), hsvRoi[:, :, 1].max(), hsvRoi[:, :, 2].max()])

    cv2.destroyAllWindows()
    return [lower, upper]


def display_result(roi):
    hsvRoi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi_result = np.concatenate((roi, hsvRoi))
    cv2.imshow('ROI Result', roi_result)


def wait_approval():
    approval = False

    key = cv2.waitKey(0)
    if key != -1 and key != ord('n'):
        approval = True
    return approval


def main():
    captureCamera()


if __name__ == '__main__':
    main()
