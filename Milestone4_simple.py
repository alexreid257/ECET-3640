#!/usr/bin/python

# ==============================================================
# ECET 3640 - Introduction to Control Engineering and Robotics
# Group 4 - Ibrahim Kone, Kyle Lawton, Alex Reid
# Autonomous Hazardous Material Retrieval Robot`
# Servos Module
#
# Target MCU: BeagleBone Black
#
# This program fulfills the requirements of Milestone 4 - the
# machine must move from the starting position on the playing
# field to the opposite end, and pick up an item placed there.
# ==============================================================

import servos_new as servos
import motors5 as motors
import leds
import time

# Initialization statements ====================================
leds.led_init()
servos.servo_init()
motors.motors_init()

# Move forward for n seconds ===================================
motors.motors_forward(0)
time.sleep(2)

# Stop =========================================================
motors.motors_stop()

# Pick up object ===============================================
servos.shoulder_move("down", 11)
servos.claw_move("close")
servos.shoulder_move("up", 8)

# Stop PWM output ==============================================
motors.motors_cleanup()

# Exit
exit()