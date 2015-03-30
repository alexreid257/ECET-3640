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

import time
import leds
import servos
import camera

# ========== Initialization ==========


def init():
    # Run LED Init
    leds.led_init()

    time.sleep(1)

    # Run Servos Init
    servos.servo_init()

    leds.led_on(0)
    time.sleep(1)

    # Run Camera Init
    camera.camera_init()

    leds.led_off(0)
    leds.led_on(1)
    time.sleep(1)


def milestone3():
    print "Running Milestone Code"
    object_position = 0

    # Camera subroutine
    # Identify if object is in position 1 or 2

    if object_position == 1:
        position_1()
    elif object_position == 2:
        position_2()
    else:
        position_null()


def position_1():
    servos.shoulder_duty = servos.shoulder_move("down", 5, servos.shoulder_duty)
    servos.elbow_duty = servos.elbow_move("down", 5, servos.elbow_duty)
    servos.claw_move("close")
    servos.shoulder_duty = servos.shoulder_move("up", 5, servos.shoulder_duty)


def position_2():
    servos.shoulder_duty = servos.shoulder_move("down", 5, servos.shoulder_duty)
    servos.elbow_duty = servos.elbow_move("up", 5, servos.elbow_duty)
    servos.claw_move("close")
    servos.shoulder_duty = servos.shoulder_move("up", 5, servos.shoulder_duty)


def position_null():
    servos.elbow_duty = servos.elbow_move("down", 10, servos.elbow_duty)


init()

loop_var = True

while loop_var:
    milestone3()
    time.sleep(30)