#!/usr/bin/python

# ==============================================================
# ECET 3640 - Introduction to Control Engineering and Robotics
# Group 4 - Ibrahim Kone, Kyle Lawton, Alex Reid
# Autonomous Hazardous Material Retrieval Robot
# Camera Module
#
# Target MCU: BeagleBone Black
#
# This module is intended to allow a program to use a USB Camera
# on the BeagleBone Black. The camera can distinguish objects
# by shape and by color.
# ==============================================================

import cv2 as cv
capture = cv.CaptureFromCAM(0)


def camera_init():
    cv.SetCaptureProperty(capture, 3, 360)
    cv.SetCaptureProperty(capture, 3, 240)
    print "Camera Initialized"


def get_image():
    img = cv.QueryFrame(capture)

    cv.Smooth(img, img, cv.CV_BLUR, 3)               # Smooth Image
    hue_img = cv.CreateImage(cv.GetSize(img), 8, 3)  # Convert the Hue
    cv.CvtColor(img, hue_img, cv.CV_BGR2HSV)         # Convert to HSV

    threshold_img = cv.CreateImage(cv.GetSize(hue_img), 8, 1)  # Create Threshold object
    cv.InRangeS(hue_img, (38, 120, 60), (75, 255, 255), threshold_img)  # Look for color (Green right now)

    storage = cv.CreateMemStorage(0)
    contour = cv.FindContours(threshold_img, storage, cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)

    points = []

    while contour:
        #

    if cv.WaitKey(10) == 27:
        exit()




