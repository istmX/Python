# from ... import ... as ...
# This form imports specific names and gives them aliases.

from math import pi as PI
from math import sqrt as square_root
from random import randint as random_integer

print("Pi:", PI)
print("Square root of 9:", square_root(9))
print("Random integer (1-100):", random_integer(1, 100))

# Why alias an imported name?
# 1. Shorter to type
from datetime import date as Date
print("Today:", Date.today())

# 2. Avoid name clashes
# If your code also has a variable named 'pi', the alias
# prevents confusion:
pi = 3.14159   # your own variable
from math import pi as math_pi
print("Your pi:", pi)
print("Math pi:", math_pi)

# 3. Follow common conventions used across the Python world
#    (e.g., import numpy as np, import pandas as pd)
