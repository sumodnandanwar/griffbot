#!/usr/bin/python
#
# NOTE - Only for use on Raspberry Pi or other SBC.
#
import time
import atexit
import threading
import random
import board
import sys, tty, termios, time
from adafruit_motor import stepper as STEPPER
from adafruit_motorkit import MotorKit

# create a default object, no changes to I2C address or frequency
kit = MotorKit(i2c=board.I2C())

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()  # pylint: disable=bad-thread-instantiation
st2 = threading.Thread()  # pylint: disable=bad-thread-instantiation

# # setting up the user input system
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    kit.stepper1.release()
    kit.stepper2.release()


atexit.register(turnOffMotors)

stepstyles = [STEPPER.SINGLE, STEPPER.DOUBLE, STEPPER.INTERLEAVE, STEPPER.MICROSTEP]


def stepper_worker(stepper, numsteps, direction, style):
    # print("Steppin!")
    for _ in range(numsteps):
        stepper.onestep(direction=direction, style=style)
    # print("Done")

move_dir = [STEPPER.FORWARD,STEPPER.BACKWARD]

while True:
    char = getch()
    if(char == "w"):
        stepper_worker(kit.stepper1,
                20,
                move_dir[0],
                stepstyles[3])
    if(char == "s"):
        stepper_worker(kit.stepper1,
                20,
                move_dir[1],
                stepstyles[3])
    if(char == "e"):
        stepper_worker(kit.stepper2,
                20,
                move_dir[0],
                stepstyles[3])
    if(char == "d"):
        stepper_worker(kit.stepper2,
                20,
                move_dir[1],
                stepstyles[3])
    if(char == "o"):
        quit()
    
    # time.sleep(0.1)

# while True:
#     if not st1.isAlive():
#         randomdir = random.randint(0, 1)
#         print("Stepper 1")
#         if randomdir == 0:
#             move_dir = STEPPER.FORWARD
#             print("forward")
#         else:
#             move_dir = STEPPER.BACKWARD
#             print("backward")
#         randomsteps = random.randint(10, 50)
#         print("%d steps" % randomsteps)
#         st1 = threading.Thread(
#             target=stepper_worker,
#             args=(
#                 kit.stepper1,
#                 randomsteps,
#                 move_dir,
#                 stepstyles[random.randint(0, 3)],
#             ),
#         )
#         st1.start()

#     if not st2.isAlive():
#         print("Stepper 2")
#         randomdir = random.randint(0, 1)
#         if randomdir == 0:
#             move_dir = STEPPER.FORWARD
#             print("forward")
#         else:
#             move_dir = STEPPER.BACKWARD
#             print("backward")
#         randomsteps = random.randint(10, 50)
#         print("%d steps" % randomsteps)
#         st2 = threading.Thread(
#             target=stepper_worker,
#             args=(
#                 kit.stepper2,
#                 randomsteps,
#                 move_dir,
#                 stepstyles[random.randint(0, 3)],
#             ),
#         )
#         st2.start()

#     time.sleep(0.1)  # Small delay to stop from constantly polling threads
    # see: https://forums.adafruit.com/viewtopic.php?f=50&t=104354&p=562733#p562733

    #LIMBO SOFTWARE PRESENTS
#RASPBERRY PI MOTOR DRIVER CONTROLS

# Importing Modules
# import time
# import RPi.GPIO as GPIO
# import sys, tty, termios, time
# import os

# # setting up the pins to use
# # you may need to change these if you are running through different pins
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(22,GPIO.OUT)
# GPIO.setup(23,GPIO.OUT)
# GPIO.setup(17,GPIO.OUT)
# GPIO.setup(18,GPIO.OUT)

# #display user controls
# print ('W forward')
# print ('S Reverse')
# print ('A Left')
# print ('D Right')
# print ('Q Stop')
# print ('E Exit Programme')

# # setting up the user input system
# def getch():
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch

# # defining the different directions
# # you may need to change these if you are using different pins
# def forward():
#     GPIO.output(22, True)
#     GPIO.output(23, False)
#     GPIO.output(17, True)
#     GPIO.output(18, False)

# def reverse():
#     GPIO.output(22, False)
#     GPIO.output(23, True)
#     GPIO.output(17, False)
#     GPIO.output(18, True)

# def right():
#     GPIO.output(22, True)
#     GPIO.output(23, False)
#     GPIO.output(17, False)
#     GPIO.output(18, False)

# def left():
#     GPIO.output(22, False)
#     GPIO.output(23, False)
#     GPIO.output(17, True)
#     GPIO.output(18, False)
    
# def stop():
#     GPIO.output(22, False)
#     GPIO.output(23, False)
#     GPIO.output(17, False)
#     GPIO.output(18, False)


# # setting up which input controls which direction 
# while True:
#     char = getch()
#     if(char == "w"):
#         forward()
#     if(char == "q"):
#         stop()
#     if(char == "s"):
#         reverse()
#     if(char == "a"):
#         left()
#     if(char == "d"):
#         right()
#     if(char == "e"):
#         quit()

# # Hope the programme works for you! enjoy!
# # Limbo Software