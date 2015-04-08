#!/usr/bin/python

# ==============================================================
# Group 4
# Motors_py
# Copyright 2015
#       Description:
#       Code that will utilize PWM for the motor inputs 1A & 2A to control
#       speed and will use GPIO output on inputs 1B & 2B to control direction.
#       
# The pins are set up as follows:
#
#       P9_21 = Motor1A PWM
#       P9_13 = Motor1B GPIO
#       P8_19 = Motor2B PWM
#       P9_15 = Motor2A GPIO
# ==============================================================


import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM


Motor1A = "P9_21"		# Sets P9_21 as motor1a
Motor1B = "P9_13"		# Sets P9_13 as motor1b
Motor2A = "P8_19"		# Sets P8_19 as motor2a
Motor2B = "P9_15"		# Sets P9_15 as motor2b INCORRECT - See header for correct pin assignments
duty_stop = 9
duty_forward = 35  # 12 is max cycle
duty_back = 6      # 6 is min cycle


# ==============================================================
# Function:  motors_init
# Returns:   None
# Arguments: None
# Summary:   Initializes PWM for motors on predefined pins,
#            at 60 Hz, at the correct polarity. Also sets up
#            GPIO outputs for H-bridge control.
# ==============================================================


def motors_init():
    PWM.start(Motor1A, duty_forward, 60.0, 1)  # Starts the PWM output
    PWM.start(Motor2A, duty_forward, 60.0, 1)
    GPIO.setup(Motor1B, GPIO.OUT)		# Sets up pins as GPIO outputs
    GPIO.setup(Motor2B, GPIO.OUT)
print "Ready"


# ==============================================================
# Function:  motors_forward
# Returns:   d (Duty cycle)
# Arguments: d (Duty cycle)
# Summary:   Sets duty cycle to d for both motors, sets GPIO
#            to move forward.
# ==============================================================


def motors_forward(d):
    PWM.set_duty_cycle(Motor1A, d)
    GPIO.output(Motor1B, GPIO.LOW)  # GPIO LOW is forward
    PWM.set_duty_cycle(Motor2A, d)
    GPIO.output(Motor2B, GPIO.LOW)
    return d
print "Forward"


# ==============================================================
# Function:  motors_reverse
# Returns:   d (Duty cycle)
# Arguments: d (Duty cycle)
# Summary:   Sets duty cycle to d for both motors, sets GPIO
#            to move reverse.
# ==============================================================


def motors_reverse():
    PWM.stop(Motor1A)
    GPIO.output(Motor1B, GPIO.HIGH)
    PWM.stop(Motor2A)
    GPIO.output(Motor2B, GPIO.HIGH)
print "Reverse"


# ==============================================================
# Motors right
# ==============================================================


def motors_right(d):
    PWM.set_duty_cycle(Motor1A, 7.5)
    GPIO.output(Motor1B, GPIO.HIGH)
    PWM.set_duty_cycle(Motor2A, d)
    GPIO.output(Motor2B, GPIO.LOW)
    PWM.stop(Motor1A)
    PWM.stop(Motor2A)
    return d
    
print "Right"


# ==============================================================
# Motors left
# ==============================================================


def motors_left(d):
    PWM.set_duty_cycle(Motor1A, d)
    GPIO.output(Motor1B, GPIO.LOW)
    PWM.set_duty_cycle(Motor2A, d)
    GPIO.output(Motor2B, GPIO.HIGH)
    return d
print "Left"

# ==============================================================
# Motors Stop
# ==============================================================


def motors_stop():
    PWM.stop(Motor1A)
    GPIO.output(Motor1B, GPIO.LOW)
    PWM.stop(Motor2A)
    GPIO.output(Motor2B, GPIO.LOW)
print "Stop"

# ==============================================================
# Motors kill
# ==============================================================

def motors__kill():
    PWM.stop(Motor1A)
    PWM.stop(Motor2A)
print "Signals Killed"

# ==============================================================
# Motors right control
# ==============================================================


def motors_right_control(dut, direction):
    if direction == "forward":
        PWM.set_duty_cycle(Motor1A, dut)
        GPIO.output(Motor1B, GPIO.LOW)
    elif direction == "backward":
        PWM.set_duty_cycle(Motor1A, dut)
        GPIO.output(Motor1B, GPIO.HIGH)
    else:
        print "Direction error"

# ==============================================================
# Motors left control
# ==============================================================


def motors_left_control(dut, direction):
    if direction == "forward":
        PWM.set_duty_cycle(Motor2A, dut)
        GPIO.output(Motor2B, GPIO.LOW)
    elif direction == "backward":
        PWM.set_duty_cycle(Motor2A, dut)
        GPIO.output(Motor2B, GPIO.HIGH)
    else:
        print "Direction Error"

# ==============================================================
# Motors Cleanup
# ==============================================================
def motors_cleanup():
    GPIO.cleanup()  # Kills all GPIO signals
    PWM.cleanup() 	# Kills all PWM signals
    exit()
