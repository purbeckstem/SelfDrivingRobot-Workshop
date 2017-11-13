#!/usr/bin/python3

from bluedot import BlueDot
from signal import pause
from gpiozero import Robot
from time import sleep


bd = BlueDot()
robot = Robot(left=(18,17), right=(23,22))

def turn_around():
    for i in range (0, 5):
        robot.left()
        sleep(0.2)
        robot.right()
        sleep(0.2)
    
def move(pos):
    if pos.top:
        robot.forward(pos.distance)
    elif pos.bottom:
        robot.backward(pos.distance)
    elif pos.left:
        robot.left(pos.distance)
    elif pos.right:
        robot.right(pos.distance)

def stop():
        robot.stop()
    
bd.when_pressed = move
bd.when_moved = move
bd.when_released = stop
bd.when_double_pressed = turn_around

pause()

