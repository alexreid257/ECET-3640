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

shoulder = "P9_22"    # Shoulder is on Bus 9, Pin 22
elbow = "P9_16"       # Elbow is on Bus 9, Pin 16
claw = "P8_13"        # Claw is on Bus 8, Pin 13

shoulder_duty = 9.0   # Shoulder starts at 9.5% duty cycle
elbow_duty = 5.5      # Elbow starts at 5.5% duty cycle
claw_duty = 14.0      # Claw starts open at 13% duty cycle


def servo_init():
    PWM.start(shoulder, shoulder_duty, 60.0)
    PWM.start(elbow, elbow_duty, 60.0)
    PWM.start(claw, claw_duty, 60.0)
    print "Servos Initialized"
    time.sleep(2)


def servo_close():
    PWM.set_duty_cycle(shoulder, 9.0)
    PWM.set_duty_cycle(elbow, 5.5)
    PWM.set_duty_cycle(claw, 14.0)
    PWM.cleanup()


def shoulder_move(direction, degrees, duty):
    duty_change = degrees * 9 / 5  # Convert from degrees to duty cycle
    if direction == "up":
        for x in range(0, duty_change):
            PWM.set_duty_cycle(shoulder, duty)
            time.sleep(0.1)
            duty -= 0.1
        return duty
    elif direction == "down":
        for x in range(0, duty_change):
            PWM.set_duty_cycle(shoulder, duty)
            time.sleep(0.1)
            duty += 0.1
        return duty
    else:
        print "OH GOD MY SHOULDER (Shoulder Direction Error)"


def elbow_move(direction, degrees, duty):
    duty_change = degrees * 9 / 5  # Convert from degrees to duty cycle
    if direction == "in":
        for x in range(0, duty_change):
            PWM.set_duty_cycle(elbow, duty)
            time.sleep(0.1)
            duty -= 0.1
        return duty
    elif direction == "out":
        for x in range(0, duty_change):
            PWM.set_duty_cycle(elbow, duty)
            time.sleep(0.1)
            duty += 0.1
        return duty
    else:
        print "My only regret... is that I have... boneitis. (Elbow Direction Error)"


def claw_move(direction):
    if direction == "open":
        for x in range(0, 35):
            duty = 16.5
            PWM.set_duty_cycle(claw, duty)
            time.sleep(0.1)
            duty -= 0.1
        return "open"
    elif direction == "close":
        for x in range(0, 35):
            duty = 13.0
            PWM.set_duty_cycle(claw, duty)
            time.sleep(0.1)
            duty += 0.1
        return "closed"
    else:
        print "This would be gruesome in real life. (Claw Direction Error)"
