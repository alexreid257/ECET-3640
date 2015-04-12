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

elbow_duty = 5.5      # Elbow starts at 5.5% duty cycle
shoulder_duty = 9.5   # Shoulder starts at 9.5% duty cycle
claw_duty = 13.0      # Claw starts open at 13% duty cycle

# ==============================================================
# Function:  servo_init
# Returns:   None
# Arguments: None
# Summary:   Initializes PWM for servos on predefined pins,
#            at 60 Hz.
# ==============================================================


def servo_init():
    PWM.start(shoulder, shoulder_duty, 60.0)
    PWM.start(elbow, elbow_duty, 60.0)
    PWM.start(claw, claw_duty, 60.0)
    print "Servos Initialized"
    time.sleep(2)

# ==============================================================
# Function:  shoulder_move
# Returns:   duty (Duty cycle)
# Arguments: direction, degrees, duty
# Summary:   Moves shoulder servo either up or down, by the
#            number of degrees specified. The "duty" argument
#            should be the current shoulder_duty. If a program
#            imports servos.py as is, the call for this function
#            would look like this:
#
# servos.shoulder_duty = servos.shoulder_move("up", 15, servos.shoulder_duty)
#
# ==============================================================


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

# ==============================================================
# Function:  elbow_move
# Returns:   duty (Duty cycle)
# Arguments: direction, degrees, duty
# Summary:   Moves elbow servo either out or in, by the
#            number of degrees specified. The "duty" argument
#            should be the current servo_duty. If a program
#            imports servos.py as is, the call for this function
#            would look like this:
#
# servos.elbow_duty = servos.elbow_move("up", 15, servos.elbow_duty)
#
# ==============================================================


def elbow_move(direction, degrees, duty):
    duty_change = degrees * 9 / 5  # Convert from degrees to duty cycle
    if direction == "up":
        for x in range(0, duty_change):
            PWM.set_duty_cycle(elbow, duty)
            time.sleep(0.1)
            duty -= 0.1
        return duty
    elif direction == "down":
        for x in range(0, duty_change):
            PWM.set_duty_cycle(elbow, duty)
            time.sleep(0.1)
            duty += 0.1
        return duty
    else:
        print "My only regret... is that I have... boneitis. (Elbow Direction Error)"

# ==============================================================
# Function:  claw_move
# Returns:   claw status (open/closed)
# Arguments: direction
# Summary:   Either opens or closes claw.
# ==============================================================


def claw_move(direction):
    if direction == "open":
        for x in range(0, 35):
            duty = 16.5
            PWM.set_duty_cycle(claw, duty)
            time.sleep(0.1)
            duty += 0.1
        return "open"
    elif direction == "close":
        for x in range(0, 35):
            duty = 13.0
            PWM.set_duty_cycle(claw, duty)
            time.sleep(0.1)
            duty -= 0.1
        return "closed"
    else:
        print "This would be gruesome in real life. (Claw Direction Error)"