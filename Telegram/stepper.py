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

