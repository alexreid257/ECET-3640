#!/usr/bin/python

# ==============================================================
# ECET 3640 - Introduction to Control Engineering and Robotics
# Group 4 - Ibrahim Kone, Kyle Lawton, Alex Reid
# Autonomous Hazardous Material Retrieval Robot
# Motors Module
#
# Target MCU: BeagleBone Black
#
# This module is intended to allow a program to control two
# motors via an H-Bridge from the BeagleBone Black.
# ==============================================================

import Adafruit_BBIO.PWM as PWM


def shutdown(motor_arg_1, motor_arg_2, motor_arg_3, motor_arg_4):
    print 'Signals Stopped'
    PWM.stop(motor_arg_1)  # Stops this motor
    PWM.stop(motor_arg_2)
    PWM.stop(motor_arg_3)
    PWM.stop(motor_arg_4)
    PWM.cleanup()  # Ends all PWM


def stop(motor_arg_1, motor_arg_2, motor_arg_3, motor_arg_4, duty_stop_arg):
    print 'stop'
    PWM.set_duty_cycle(motor_arg_1, duty_stop_arg)
    PWM.set_duty_cycle(motor_arg_2, duty_stop_arg)
    PWM.set_duty_cycle(motor_arg_3, duty_stop_arg)
    PWM.set_duty_cycle(motor_arg_4, duty_stop_arg)


def go_forward(motor_arg_1, motor_arg_2, duty_forward_arg):
    print 'forward'
    PWM.set_duty_cycle(motor_arg_1, duty_forward_arg)
    PWM.set_duty_cycle(motor_arg_2, duty_forward_arg)


def go_backward(motor_arg_1, motor_arg_2, duty_back_arg):
    print 'backward'
    PWM.set_duty_cycle(motor_arg_1, duty_back_arg)
    PWM.set_duty_cycle(motor_arg_2, duty_back_arg)


def go_left(motor_arg_1, motor_arg_2, duty_forward_arg, duty_back_arg):
    print 'left'
    PWM.set_duty_cycle(motor_arg_1, duty_forward_arg)
    PWM.set_duty_cycle(motor_arg_2, duty_back_arg)


def go_right(motor_arg_1, motor_arg_2, duty_back_arg, duty_forward_arg):
    print 'right'
    PWM.set_duty_cycle(motor_arg_1, duty_back_arg)
    PWM.set_duty_cycle(motor_arg_2, duty_forward_arg)


def go_up(motor_arg_1, motor_arg_2, duty_forward_arg):
    print 'up'
    PWM.set_duty_cycle(motor_arg_1, duty_forward_arg)
    PWM.set_duty_cycle(motor_arg_2, duty_forward_arg)


def go_down(motor_arg_1, motor_arg_2, duty_back_arg):
    print 'down'
    PWM.set_duty_cycle(motor_arg_1, duty_back_arg)
    PWM.set_duty_cycle(motor_arg_2, duty_back_arg)


def motors_init():
    motor1a = "P9_21"
    motor1b = "P9_29"
    motor2a = "P8_45"
    motor2b = "P8_46"
    duty_stop = 9
    duty_forward = 12  # 12 is max cycle
    duty_back = 6 	   # 6  is min cycle
    PWM.start(motor1a, duty_stop, 60.0, 1)
    PWM.start(motor1b, duty_stop, 60.0, 1)
    PWM.start(motor2a, duty_stop, 60.0, 1)
    PWM.start(motor2b, duty_stop, 60.0, 1)
    print "Ready"
#
# key = '0'
# while key != 'q':
#     key = raw_input(">")
#     if key == '1':		    # Forward press 1
#         go_forward(Motor1A, Motor2A, duty_forward)
#     elif key == '2':		# Backward press 2
#         go_backward(Motor1A, Motor2A, duty_back)
#     elif key == '3':		# Left press 3
#         go_left(Motor1A, Motor2A, duty_forward, duty_back)
#     elif key == '4':		# Right press 4
#         go_right(Motor1A, Motor2A, duty_back, duty_forward)
#     elif key == '5':		# Up press 5
#         go_up(Motor1B, Motor2B, duty_forward)
#     elif key == '6':		# Down press 6
#         go_down(Motor1B, Motor2B, duty_back)
#     elif key == '7':		# Stop press 7
#         stop(Motor1A, Motor1B, Motor2A, Motor2B, duty_stop)
#     elif key == '8':		# Shutdown
#         shutdown(Motor1A, Motor1B, Motor2A, Motor2B)
#
# PWM.cleanup()  # stop all signals
