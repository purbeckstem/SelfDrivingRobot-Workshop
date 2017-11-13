# SelfDrivingRobot-Workshop
Code repository for Self Driving Robot Workshop.

Here is the  code and files to run a robotics workshop loosely based around self driving cars.Firstly, we create robots that can be remotely controlled over bluetooth using Raspberry Pi computers. 

The robots are built using the excellent CamJam Edukit 3 kits, by using Daniel Bull's 3d printed chassis. https://www.thingiverse.com/thing:1113796
using Martin O'Hanlon's excellent Bluedot python library http://bluedot.readthedocs.io/en/latest/
as well as Ben Nuttall's gpiozero python library. http://bluedot.readthedocs.io/en/latest/gettingstarted.html 

The workshop runs over the course of a school day, and basically is broken down into 5x  1 hour sections: 
1. Assembly and getting bluedot control code to work. 
2. Customisation of robots using bluetooth gestures. Driving course.
3. Line follower module install and coding. Robots follow line loop with code optimisation.
4. Ultrasonic distance sensor install - crash prevention coding. 
5. Testing out optimised code / sumo championship.  


Session 1 - Getting bluedot to work -  depending on ability of coders, can have anything from digital d-pad style control to analogue levels of input sensitivity using the BlueDot application that can be run on a tablet. 
learn the basis of input devices, using the BlueDot python library to make more sophisticated input, such as double clicking, swiping, analogue sliders.  This is used to code more complicated behaviour for the robots and to personalise their creations, for example: playing a sound file to identify their robot, shining a particular colour LED to identify their robot, flash a light in a secret code sequence (morse), or perhaps perform a taunt manouevre.  
2: Once they have managed to code the basic input controllers, they will be expected to use the tablets to control the robots through an assault course comprising of a slalom, rough terrain, slopes, and width restrictions.  They will be timed, incurring penalities for collisions with the surroundings.  
3: Next, the teams will add a line-following module to their robots, involving basic electronics and soldering.  The module will need to be coded in order to get their robots to follow a line around a loop with different sections (hairpins, straights, chicanes, branches).  The code will mostly be provided, but can be optimised to speed up their 'bots.  Groups that optimise their code will score more highly by finishing faster and gaining higher scores.  
4: Lastly, the groups will attempt to add an ultrasonic distance sensor to their cars.  These work similarly to echolocation in bats and dolphins, and are similar to the LIDAR systems used in autonomous vehicles. Once the modules are installed, they can be used to ensure that the car never crashes into anything whilst moving forward, or that it modulates speed as it gets nearer to another car.  Cars which collide with other cars will be penalised as they move around the simple loop.   
A final hurrah for the day will be a chance to get to the robots to play Sumo to try and outmanouevre each other in a ring, and also to Joust each other with balloons and a pin.
