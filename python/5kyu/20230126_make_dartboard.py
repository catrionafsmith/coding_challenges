#  5kyu Create your own mechanical dartboard that gives back your score based on the coordinates of your dart.
# The coordinates are `(x, y)` are always relative to the center of the board (0, 0). The unit is millimeters. If you throw your dart 5 centimeters to the left and 3 centimeters below, it is written as:
# score = get_score(-50, -30)

# Possible scores are:
# Outside of the board: `"X"`
# Bull's eye: `"DB"`
# Bull: `"SB"`
# A single number, example: `"10"`
# A triple number: `"T10"`
# A double number: `"D10"`


# My ideas:
# The dartboard areas are circles - do I need to convert my co-ordinates radially?
# Would multiplying them together make sense? (Probably not as then a score of 1 would be the same as a 20)
# Could start with returning an X if the dart is out of bounds.
# Can use absolute values of numbers
# To get the distance from the centre we can use Pythagoras: x**2 + y**2 = z**2
from math import *

def get_score(x,y):
    score = ""
    dist_from_centre = sqrt(x**2 + y**2)
    if (dist_from_centre) > 170:
        return "X"
    elif (dist_from_centre) > 162:
        score += "D"
    elif 99 > (dist_from_centre) > 107:
        score += "T"
    elif (dist_from_centre) < 6:
        return "DB"
    elif (dist_from_centre) < 16:
        return "SB"
    angle = degrees(atan(y/x))
    print(angle)
    if x > 0 and y >0:
        if angle < 9:
            score += "6"
        elif angle < 27:
            score += "13"
        elif angle < 45:
            score += "4"
        elif angle < 63:
            score += "18"
        elif angle < 81:
            score += "1"
        elif angle < 99:
            score += "20"
    elif x < 0 and y >0:
        if 0 < angle < 9:
            score += "6"
        elif 9 < angle < 27:
            score += "13"
        elif 27 < angle < 45:
            score += "4"
        elif 45 < angle < 63:
            score += "18"


    return score

# get_score(-73.905, -95.94)
# get_score(55.53, -87.95)
# print(get_score(55.53, 55))
# print(get_score(45, 45))
get_score(-5.43, 117.95)