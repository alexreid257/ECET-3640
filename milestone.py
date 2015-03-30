#----------------------------------------------------------------
#FILE NAME: Milestone2.py 
#DATE     : 3 Mar 2015
#TARGET MCU  : Beaglebone Black
#DESCRIPTION : This is the code for Milestone 2 that will control
#			   the duty cycles for each of the 3 servos used to
#			   manipulate the robotic arm that will retrieve spill 
#			   material
#---------------------------------------------------------------
import Adafruit_BBIO.PWM as PWM
import time
servo1 = "P9_22"
servo2 = "P9_16"
servo3 = "P8_13"

#------------------servos initialization------------------------
duty1 = 9.5
duty2 = 5.5
duty3 = 13.0
PWM.start(servo1, duty1, 60.0)
PWM.start(servo2, duty2, 60.0)
PWM.start(servo3, duty3, 60.0)
time.sleep(2)

#-------------------move robot arm down and pick up object---------------------
for x in range(0,15):
	PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 -= 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,50):
        PWM.set_duty_cycle(servo2, duty2)
        time.sleep(0.1)
        duty2 += 0.1
print "Setting duty2 to %s" %duty2
for x in range(0,27):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 += 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,35):
	PWM.set_duty_cycle(servo3, duty3)
        time.sleep(0.1)
        duty3 += 0.1
print "Setting duty3 to %s" %duty3

#-----------move robot arm up and drop object--------
for x in range(0,27):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 -= 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,50):
        PWM.set_duty_cycle(servo2, duty2)
        time.sleep(0.1)
        duty2 -= 0.1
print "Setting duty2 to %s" %duty2
for x in range(0,15):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 += 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,35):
        PWM.set_duty_cycle(servo3, duty3)
        time.sleep(0.1)
        duty3 -= 0.1
print "Setting duty3 to %s" %duty3
time.sleep(3)

#----------------move robot and pick up object------
for x in range(0,3):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 += 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,35):
        PWM.set_duty_cycle(servo3, duty3)
        time.sleep(0.1)
        duty3 += 0.1
print "Setting duty3 to %s" %duty3

#---------------------move robot arm down and drop object-------------------
for x in range(0,17):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 -= 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,50):
        PWM.set_duty_cycle(servo2, duty2)
        time.sleep(0.1)
        duty2 += 0.1
print "Setting duty2 to %s" %duty2
for x in range(0,27):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 += 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,35):
        PWM.set_duty_cycle(servo3, duty3)
        time.sleep(0.1)
        duty3 -= 0.1
print "Setting duty3 to %s" %duty3

#---------------------move robot arm in initial position-------------------
for x in range(0,25):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 -= 0.1
print "Setting duty1 to %s" %duty1
for x in range(0,50):
        PWM.set_duty_cycle(servo2, duty2)
        time.sleep(0.1)
        duty2 -= 0.1
print "Setting duty2 to %s" %duty2
for x in range(0,15):
        PWM.set_duty_cycle(servo1, duty1)
        time.sleep(0.1)
        duty1 += 0.1
print "Setting duty1 to %s" %duty1

#----------------------------------------
while True:
        angle = raw_input("x to exit:")
        if angle == 'x':
                PWM.stop(servo1)
                PWM.stop(servo2)
                PWM.stop(servo3)
                PWM.cleanup()
                break
        else:
		if float(angle) < 0 or float(angle) > 180:
                	print "Invalid command"
