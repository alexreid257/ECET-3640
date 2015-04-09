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
    print "Forward"
    return d

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
# Function:  motors_right
# Returns:   None
# Arguments: None
# Summary:   Sets duty cycle to the same value for both motors,
#            but in opposite directions to accomplish a zero-
#            degree right turn.
# ==============================================================

def motors_right():
    PWM.set_duty_cycle(Motor1A, 7.5)
    GPIO.output(Motor1B, GPIO.HIGH)
    PWM.set_duty_cycle(Motor2A, 7.5)
    GPIO.output(Motor2B, GPIO.LOW)
    PWM.stop(Motor1A)
    PWM.stop(Motor2A)
    print "Right"


# ==============================================================
# Function:  motors_left
# Returns:   None
# Arguments: None
# Summary:   Sets duty cycle to the same value for both motors,
#            but in opposite directions to accomplish a zero-
#            degree left turn.
# ==============================================================


def motors_left():
    PWM.set_duty_cycle(Motor1A, 7.5)
    GPIO.output(Motor1B, GPIO.LOW)
    PWM.set_duty_cycle(Motor2A, 7.5)
    GPIO.output(Motor2B, GPIO.HIGH)
    print "Left"

# ==============================================================
# Function:  motors_stop
# Returns:   None
# Arguments: None
# Summary:   Stops motors
# ==============================================================


def motors_stop():
    PWM.stop(Motor1A)
    GPIO.output(Motor1B, GPIO.LOW)
    PWM.stop(Motor2A)
    GPIO.output(Motor2B, GPIO.LOW)
print "Stop"

# ==============================================================
# Function:  motors_right_control
# Returns:   None
# Arguments: dut (Duty cycle), direction)
# Summary:   Direct control of right motor, in case a program
#            accessing this library needs to do so
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
# Function:  motors_left_control
# Returns:   None
# Arguments: dut (Duty cycle), direction)
# Summary:   Direct control of left motor, in case a program
#            accessing this library needs to do so
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
# Function:  motors_cleanup
# Returns:   None
# Arguments: None
# Summary:   Stops all control of motors and servos
# ==============================================================


def motors_cleanup():
    GPIO.cleanup()  # Kills all GPIO signals
    PWM.cleanup() 	# Kills all PWM signals
    exit()
