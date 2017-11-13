#!/usr/bin/python3

from bluedot import BlueDot
from signal import pause
from gpiozero import Robot

def say_hello():
    print("Hello World")

bd = BlueDot()
robot = Robot(left=(18,17), right=(23,22))

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

pause()

