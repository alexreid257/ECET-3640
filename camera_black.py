#!/usr/bin/python

# ==============================================================
# ECET 3640 - Introduction to Control Engineering and Robotics
# Group 4 - Ibrahim Kone, Kyle Lawton, Alex Reid
# Autonomous Hazardous Material Retrieval Robot
# Milestone 3
#
# This code causes the robot to scan for an object of a given
# color, then if found, pick that object up. If no objects of
# the given color are found, the robot retracts its arm.
# ==============================================================

import cv2
import numpy as np
import math
import servos
import time

# Initialize Servos
servos.servo_init()
time.sleep(2)

# Arm to scanning position
servos.elbow_duty = servos.elbow_move("out", 35, servos.elbow_duty)

# Initialize Camera

c = cv2.VideoCapture(0)
c.set(3, 320)
c.set(4, 240)
width,height = c.get(3),c.get(4)
print "frame width and height : ", width, height
cw= width/2
ch= height/2
lower_red = np.array([155,90,160])
upper_red = np.array([180,130,200])
lower_black = np.array([90,115,45])
upper_black = np.array([130,155,85])

def position_1():
    print "retrieving from position 1 (further from robot)"
    servos.claw_move("open")
    servos.shoulder_duty = servos.shoulder_move("down", 10, servos.shoulder_duty)
    servos.claw_move("close")
    servos.shoulder_duty = servos.shoulder_move("up", 10, servos.shoulder_duty)


def position_2():
    print "retrieving from position 2 (closer to robot)"
    servos.claw_move("open")
    servos.elbow_duty = servos.elbow_move("in", 15, servos.elbow_duty)
    servos.shoulder_duty = servos.shoulder_move("down", 12, servos.shoulder_duty)
    servos.claw_move("close")
    servos.shoulder_duty = servos.shoulder_move("up", 12, servos.shoulder_duty)

loopvar = 1

while loopvar:
	_,f = c.read()
	frame = cv2.flip(f,1)
	blur =cv2.blur(frame,(3,3))
	cv2.circle(frame,(int(cw),int(ch)),1,[0,255,0],2)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
	mask_red = cv2.inRange(hsv, lower_red, upper_red)
	mask_black = cv2.inRange(hsv, lower_black, upper_black)

	contours_red,hierarchy = cv2.findContours(mask_red,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	contours_black,hierarchy = cv2.findContours(mask_black,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	
	#if countours_red is not None:
	for cnt in contours_red:
		x,y,w,h = cv2.boundingRect(cnt)
		cx,cy = x+w/2, y+h/2
		cv2.rectangle(frame,(x,y),(x+w,y+h),[255,0,0],1)
		cv2.circle(frame,(cx,cy),1,[0,255,0],2)
		pst_red = cy-ch
		print "red position : ", pst_red
		if spt_red >= 0 :
		
		elif

	for cnt in contours_black:
		x,y,w,h = cv2.boundingRect(cnt)
		cx,cy = x+w/2, y+h/2
		cv2.rectangle(frame,(x,y),(x+w,y+h),[0,0,255],1)
		cv2.circle(frame,(cx,cy),1,[0,255,0],2)

	res = cv2.bitwise_and(frame,frame, mask = mask_red) 
	cv2.imshow('img', frame)

	if cv2.waitKey(25) == 27:
		break

cv2.destroyAllWindows()
c.release()
