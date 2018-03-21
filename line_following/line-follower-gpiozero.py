###Coded entirely by Gantelope: https://gist.github.com/Gantelope/ac1f62d91b35cf6a9144e6ce1885718c ### 
### used, as I thought there was a problem with my line following code, but I had plugged in the VCC, GND, and signal wires muddled.  

###Plug your line sensor module into the following pins
### VCC :   3V3 on motor controller 
### GND :   GND on motor controller
### OUT :   GPIO 25 on motor controller.

##tested and working with Mr Davids' robot.  
# Original code had robot with drive wheels at front - may need to swap robot.left and robot.right in the code to get it to turn the correct way when seeking  
from gpiozero import CamJamKitRobot
from gpiozero import Button
import time
 
pinLineFollower = 25
sensor = Button(pinLineFollower)
 
robot = CamJamKitRobot()
 
# Return True if the line detector is over a black line
def IsOverBlack():
    if sensor.is_pressed:
        return True
    else:
        return False
 
# Search for the black line
def SeekLine():
    print("Seeking the line")
    # The direction the robot will turn - True = Left
    Direction = True
    SeekSize = 0.2 # Turn time
    SeekCount = 1 # A count of times the robot has looked for the line
    MaxSeekCount = 5 # The maximum time to seek the line in one direction
 
    # Turn the robot left and right until it finds the line
    # Or it has been searched for long enough
    while SeekCount <= MaxSeekCount:
        # Set the seek time
        SeekTime = SeekSize * SeekCount
 
        # Start the motors turning in a direction
        if Direction:
            print("Looking left")
              robot.left(0.4)
        else:
            print("Looking Right")
              robot.right(0.4)
 
        # Save the time it is now
        StartTime = time.time()
 
        # While the robot is turning for SeekTime seconds
        # check to see whether the line detector is over black
        while time.time() - StartTime <= SeekTime:
            if IsOverBlack():
                robot.stop()
                return True
 
        # The robot has not not found the black line yet, so stop
        robot.stop()
 
          time.sleep(0.1)
 
        # Increase the seek count
        SeekCount += 1
 
        # Change direction
        Direction = not Direction
 
    # The line wasn't found
    return False
 
try:
    print("Following the line")
    while True:
        if IsOverBlack():
            robot.forward(0.4)
        else:
            robot.stop()
            if SeekLine() == False:
                robot.stop()
                print("The robot has lost the line")
                exit()
            else:
                print("Following the line")
 
except KeyboardInterrupt:
    robot.stop()
    exit()
