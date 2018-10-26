#!/usr/bin/env python

import numpy as np
import cv2
import sys
import color_detection as cd
import video_detection as vd


def detection_area():
    left = False
    if len(sys.argv) > 1 and sys.argv[1] == 'left':
        left = True
    return left


def main():
    left = detection_area()
    video_capture = cv2.VideoCapture(0)
    lower_color = np.array([0, 50, 120], dtype=np.uint8)
    upper_color = np.array([180, 150, 250], dtype=np.uint8)

    while True:
        _, frame = video_capture.read()
        frame = cv2.flip(frame, 1)

        cv2.putText(frame, 'Welcome', (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (255, 0, 0), 3, cv2.LINE_AA)

        cv2.imshow('VCOM Project', frame)
        key = cv2.waitKey(10)
        if key != -1:
            cv2.destroyAllWindows()
            video_capture.release()
            break

    if key == ord('v'):
        vd.hand_detection(lower_color, upper_color, left)
    elif key == ord('h'):
        cd.draw_contours(lower_color, upper_color)


if __name__ == '__main__':
    main()