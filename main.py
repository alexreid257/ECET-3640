#!/usr/bin/python

# ==============================================================
# ECET 3640 - Introduction to Control Engineering and Robotics
# Group 4 - Ibrahim Kone, Kyle Lawton, Alex Reid
# Autonomous Hazardous Material Retrieval Robot
# Final Code
#
# This robot is designed to autonomously differentiate between
# four different types of material, retrieve them, and place
# them in the appropriate receptacles. The materials are
# differentiated by shape and color (Nuts/Sleeves, Red/Black).
# Materials of different color are not to touch or the facility
# is assumed to be destroyed. Robots will perform their duties
# two at a time, each responsible for one side of the field.
# Each side will contain drop locations for each type of one
# color, and the robots will have to transfer materials of the
# other side's color to the robot on the other side. The pieces
# of material will be randomly distributed.
#
# Platform: BeagleBone Black Rev. C
#
# Our robot's procedure will be as follows:
#
# - Initialize
#   - Check connection to camera
#   - Position servos in init position
#   - Turn right, then left
#   - Verify turns with position sensor
# - Check in with opposing robot
#   - Transmit start code through XBEE
# - Check surrounding area with camera
# - Begin sweep along dividing wall
#   - Move forward, detecting for objects with object sensor/camera
#   - When sweep is complete, send "CLEAR" signal through XBEE
# - Sweep in ~5cm rows
# - Add opposing-colored material to bin
# - When object of our color is found, move it to the appropriate receptacle
# - When complete, if "CLEAR" signal received from other robot, dump material.
# - Sweep field once more for clarity
# - Hold indefinitely
# ==============================================================

import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
import motors2 as motor
import leds
import servos
import camera
import position

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

    # Run Motor Init
    motor.motors_init()

    leds.led_on(0)
    time.sleep(1)

    # Run Position Init
    position.position_init()

    leds.led_off(0)
    leds.led_off(1)
    leds.led_on(2)
    time.sleep(1)


def loop():
    time.sleep(2)

run(init, loop)