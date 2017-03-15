"""Python PI calculation from random numbers.

pirand.py
MIT Licence (c) 2017 Simone Cingano
Based on a video by Matt Parker (https://www.youtube.com/watch?v=RZBhSi_PwHU)

Usage: python pirand.py [faces] [rolls]
faces: how many faces per dice
rolls: how many rolls (we roll 2 dice together, 500 rolls gives 1000 numbers)
"""

import sys
import math
import random

# greater common divisor (on python 3.5 use math.gcd)
from fractions import gcd


def drawProgressBar(factor, length=20, fill="=", empty=" "):
    """Draw an updatable progress bar.
    
    Thanks to Jacob Tsui http://stackoverflow.com/a/15801617/7142433
    """
    sys.stdout.write("\r")
    progress = ""
    for i in range(length):
        if i < int(length * factor):
            progress += fill
        else:
            progress += empty
    sys.stdout.write("[%s] %.2f%%" % (progress, factor * 100))
    sys.stdout.flush()


if __name__ == "__main__":
    dice_faces = 120  # default is d120
    dice_rolls = 500  # default is 500 rolls
    # how many rolls gave out a pair of numbers that share only 1 as factor
    coprimes_counter = 0

    # get the faces and rolls from arguments
    if len(sys.argv) >= 2:
        dice_faces = int(sys.argv[1])
    if len(sys.argv) >= 3:
        dice_rolls = int(sys.argv[2])

    print "%s random rolls of two d%s" % (dice_rolls, dice_faces)
    # let's roll
    random.seed()
    for roll_index in range(dice_rolls):
        dice_one = random.randint(1, dice_faces)
        dice_two = random.randint(1, dice_faces)
        if gcd(dice_one, dice_two) == 1:
            # numbers are coprime when their only factor is 1
            coprimes_counter += 1
        if roll_index % 10000 == 0:
            drawProgressBar(roll_index / float(dice_rolls))
            
    drawProgressBar(1)
    print "\r"

    if dice_rolls == 0:
        # this happens when there are very few rolls and we get no coprimes
        print "We need to roll more to get at least 1 pair of coprimes"
    else:
        # x = coprimes / total rolls
        # pi ~= sqrt(6/x)
        guessed_pi = math.sqrt(
            6.0 / (float(coprimes_counter) / float(dice_rolls)))
        percentage_error = abs((guessed_pi - math.pi) / math.pi * 100)

        print "%s (%.5f%% error)" % (guessed_pi, percentage_error)
