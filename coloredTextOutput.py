#this function picks a random color for the output each time we run the code.

import random
from sty import fg

def generateRGB():
    red = random.randint(0,256)
    green = random.randint(0,256)
    blue = random.randint(0,256)
    return red, green, blue

def generateColour(red, green, blue):
    return fg(red, green, blue)
colour = generateColour(red, green, blue)
print(generateColour(colour, "I am Light") )

