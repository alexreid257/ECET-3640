#!/usr/bin/python

# ==============================================================
# ECET 3640 - Introduction to Control Engineering and Robotics
# Group 4 - Ibrahim Kone, Kyle Lawton, Alex Reid
# Autonomous Hazardous Material Retrieval Robot
# Servos Module
#
# Target MCU: BeagleBone Black
#
# This module is intended to allow a program to control servos
# using the BeagleBone Black GPIO. The servos should be in pins
# P922, P916, and P813. They are controlled via PWM.
# ==============================================================

import Adafruit_BBIO.PWM as PWM
import time
import math

shoulder = "P9_22"    # Shoulder is on Bus 9, Pin 22
elbow = "P9_16"       # Elbow is on Bus 9, Pin 16
claw = "P8_13"        # Claw is on Bus 8, Pin 13

shoulder_duty = 9.0   # Shoulder starts at 9.5% duty cycle
elbow_duty = 14.0     # Elbow starts at 5.5% duty cycle
claw_duty = 7.0       # Claw starts open at 13% duty cycle


def servo_init():
    PWM.start(shoulder, shoulder_duty, 60.0)
    PWM.start(elbow, elbow_duty, 60.0)
    PWM.start(claw, claw_duty, 60.0)
    time.sleep(2)
    global elbow_duty
    for x in range(0, int(abs(elbow_duty-7)*10)):
        PWM.set_duty_cycle(elbow, elbow_duty)
        time.sleep(0.05)
        elbow_duty -= 0.1
    print "elbow_duty", elbow_duty
    

def servo_stop():
    PWM.stop(shoulder)
    PWM.stop(elbow)
    PWM.stop(claw)
    PWM.cleanup()


def shoulder_move(direction, duty):
    global shoulder_duty
    if direction == "up":
        for x in range(0, int(abs(shoulder_duty-duty)*10)):
            PWM.set_duty_cycle(shoulder, shoulder_duty)
            time.sleep(0.1)
            shoulder_duty -= 0.1
        print "Shoulder duty: ", shoulder_duty
        return shoulder_duty
    elif direction == "down":
        for x in range(0, int(abs(shoulder_duty-duty)*10)):
            PWM.set_duty_cycle(shoulder,  shoulder_duty)
            time.sleep(0.1)
            shoulder_duty += 0.1
        print "Shoulder duty: ", shoulder_duty
        return shoulder_duty
    else:
        print "OH GOD MY SHOULDER (Shoulder Direction Error)"


def elbow_move(direction, duty):
    global elbow_duty
    if direction == "in":
        for x in range(0, int(abs(elbow_duty-duty)*10)):
            PWM.set_duty_cycle(elbow, elbow_duty)
            time.sleep(0.1)
            elbow_duty += 0.1
        print "elbow duty: ", elbow_duty
        return elbow_duty
    elif direction == "out":
        for x in range(0, int(abs(elbow_duty-duty)*10)):
            PWM.set_duty_cycle(elbow,  elbow_duty)
            time.sleep(0.1)
            elbow_duty -= 0.1
        print "elbow duty: ", elbow_duty
        return elbow_duty
    else:
        print "My only regret... is that I have... boneitis. (Elbow Direction Error)"


def claw_move(direction):
    global claw_duty
    if direction == "open":
        claw_duty = 7
        PWM.set_duty_cycle(claw, claw_duty)
        return "open"
    elif direction == "close":
        for x in range(0, int(abs(claw_duty-4)*10)):
            PWM.set_duty_cycle(claw, claw_duty)
            time.sleep(0.1)
            claw_duty -= 0.1
        return "closed"
    else:
        print "This would be gruesome in real life. (Claw Direction Error)"
