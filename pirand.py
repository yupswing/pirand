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


def drawProgressBar(factor, error):
    """Draw an updatable progress bar.

    Thanks to Jacob Tsui http://stackoverflow.com/a/15801617/7142433
    """
    length = 20
    fill = "="
    empty = " "
    sys.stdout.write("\r")
    progress = ""
    for i in range(length):
        if i < int(length * factor):
            progress += fill
        else:
            progress += empty
    sys.stdout.write("progress [%s] %.1f%% | current error %.5f%% " %
                     (progress, factor * 100, error))
    sys.stdout.flush()


def calculatePi(dice_rolls, coprimes_counter):
    """Calculate PI from total rolls and number of coprimes.

    Returns: (calculated_pi, percentage_error)
    """
    # x = coprimes / total rolls
    # pi ~= sqrt(6/x)
    if coprimes_counter == 0:
        return (0.0, 100.0)
    calculated_pi = math.sqrt(
        6.0 / (coprimes_counter / float(dice_rolls)))
    percentage_error = abs((calculated_pi - math.pi) / math.pi * 100)
    return calculated_pi, percentage_error


if __name__ == "__main__":
    calculate_best = True  # False to make it faster (no real time statistics)

    dice_faces = 120  # default is d120
    dice_rolls = 500  # default is 500 rolls

    # how many rolls gave out a pair of numbers that share only 1 as factor
    coprimes_counter = 0
    percentage_error = 0

    # get the faces and rolls from arguments
    if len(sys.argv) >= 2:
        dice_faces = int(sys.argv[1])
    if len(sys.argv) >= 3:
        dice_rolls = int(sys.argv[2])

    print "%s random rolls of two d%s" % (dice_rolls, dice_faces)
    # let's roll
    random.seed()
    feedback = int(dice_rolls / 1000)
    lowest_error_percentage = 100.0
    lowest_error_rolls = 0
    lowest_error_pi = 0
    if feedback < 1:
        feedback = 1
    for roll_index in range(dice_rolls):
        dice_one = random.randint(1, dice_faces)
        dice_two = random.randint(1, dice_faces)
        if gcd(dice_one, dice_two) == 1:
            # numbers are coprime when their only factor is 1
            coprimes_counter += 1
        if calculate_best:
            # calculate PI and percentage error on every roll
            # (intensive but let the program to keep track of the
            #  best calculated PI over all the rolls and show the current
            #  error to the user)
            calculated_pi, percentage_error = calculatePi(
                roll_index + 1, coprimes_counter)
            if lowest_error_percentage > percentage_error:
                lowest_error_percentage = percentage_error
                lowest_error_rolls = roll_index
                lowest_error_pi = calculated_pi
        if roll_index % feedback == 0:
            drawProgressBar(roll_index / float(dice_rolls), percentage_error)

    if coprimes_counter == 0:
        # this happens when there are very few rolls and we get no coprimes
        drawProgressBar(1, percentage_error)
        print "\r"
        print "We need to roll more to get at least 1 pair of coprimes"
    else:
        calculated_pi, percentage_error = calculatePi(
            dice_rolls, coprimes_counter)
        drawProgressBar(1, percentage_error)
        print "\r"
        print " math.pi | %.11f" % (math.pi)
        print "   Final | %.11f (%.10f%% error)" % (calculated_pi, percentage_error)
        if calculate_best:
            print "    Best | %.11f (%.10f%% error at the roll number %s)" % (lowest_error_pi, lowest_error_percentage, lowest_error_rolls)
