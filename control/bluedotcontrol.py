#!/usr/bin/python3

from bluedot import BlueDot # import the bluedot class
from signal import pause    #needed by gpiozero to run the loop
from gpiozero import Robot  #gpiozero has a robot class that makes coding the bots very easy
from time import sleep


bd = BlueDot()  
robot = Robot(left=(18,17), right=(23,22))     #motor pin assignments- these were for Ryantek controller V1.3

def turn_around():                             #Taunt manouevre that is called when bluedot detects a double click
    for i in range (0, 5):                      # repeat the following code 5 times. 
        robot.left()
        sleep(0.2)
        robot.right()
        sleep(0.2)
    
def move(pos):                                 #Move by an amount that is proportional to the position of the joystick.  
    if pos.top:
        robot.forward(pos.distance)
    elif pos.bottom:
        robot.backward(pos.distance)
    elif pos.left:
        robot.left(pos.distance)
    elif pos.right:
        robot.right(pos.distance)

def stop():                                     #stop when nothing is pressed
        robot.stop()
    
bd.when_pressed = move                          #initiate robot movement from the move function when button pressed
bd.when_moved = move                            #again, but for when you move your finger on the blue dot
bd.when_released = stop                         #stop moving when the bluedot is released
bd.when_double_pressed = turn_around            #taunt gesture added for showboating, defined above

pause()                                         #keep the script running forever. 

