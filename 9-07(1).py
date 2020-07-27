import math
from decimal import *

def distance(x1, y1, x2, y2):
    x = (x1-x2)**2
    y = (y1-y2)**2
    return round(math.sqrt(x+y),2)

distance(1, 1, 0, 0)