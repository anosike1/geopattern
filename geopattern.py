# import the turtle module
from turtle import *

# set the speed of the turtle to fastest
speed ("fastest")
# create a loop to run 100 times
for steps in range(100):
    # for each run, another loop runs which changes the color
    for c in ('blue', 'red', 'green', 'black'):
        
        # moves forward in increasing number of steps
        forward(steps)
        # and goes right by 40 degress
        right(40)
        color(c)

# afterward, the turtle comes home
penup()
home()
# activate the program
mainloop()