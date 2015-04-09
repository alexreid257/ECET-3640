#!/usr/bin/python

# ==============================================================
# ECET 3640 - Introduction to Control Engineering and Robotics
# Group 4 - Ibrahim Kone, Kyle Lawton, Alex Reid
# Autonomous Hazardous Material Retrieval Robot
# LEDs Module
#
# Target MCU: BeagleBone Black
#
# This module is intended to allow a program to control the
# on-board LEDs on the BeagleBone Black.
# ==============================================================

import time

# ON-BOARD LEDs definitions

led0 = "/sys/class/leds/beaglebone:green:usr0/brightness"
led1 = "/sys/class/leds/beaglebone:green:usr1/brightness"
led2 = "/sys/class/leds/beaglebone:green:usr2/brightness"
led3 = "/sys/class/leds/beaglebone:green:usr3/brightness"

# ==============================================================
# Function:  led_on
# Returns:   None
# Arguments: num (LED number)
# Summary:   Turns on on-board LED of the specified number
# ==============================================================


def led_on(num):
    if num == 0:
        open(led0, 'w').write("1")
    elif num == 1:
        open(led1, 'w').write("1")
    elif num == 2:
        open(led2, 'w').write("1")
    elif num == 3:
        open(led3, 'w').write("1")
    else:
        print "Help Help, I'm being repressed! (LEDs number error)"

# ==============================================================
# Function:  led_off
# Returns:   None
# Arguments: num (LED number)
# Summary:   Turns off on-board LED of the specified number
# ==============================================================


def led_off(num):
    if num == 0:
        open(led0, 'w').write("0")
    elif num == 1:
        open(led1, 'w').write("0")
    elif num == 2:
        open(led2, 'w').write("0")
    elif num == 3:
        open(led3, 'w').write("0")
    else:
        print "Help Help, I'm being repressed! (LEDs number error)"

# ==============================================================
# Function:  led_init
# Returns:   None
# Arguments: None
# Summary:   Initializes on-board LEDs by turning each on and
#            off in turn.
# ==============================================================


def led_init():
    for i in range(4):
        led_off(i)

    for i in range(4):
        led_on(i)
        time.sleep(1)
        led_off(i)
        time.sleep(1)