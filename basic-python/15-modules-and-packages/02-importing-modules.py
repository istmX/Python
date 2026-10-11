# Importing Modules
# There are several ways to import.

# 1. Import the whole module
import math
print("Whole module:", math.pi)

# 2. Import specific names from a module
from math import pi, sqrt
print("Specific names:", pi, sqrt(25))

# 3. Import a module with an alias (short nickname)
import random as rnd
print("With alias:", rnd.randint(1, 6))

# 4. Import everything (generally NOT recommended)
# from math import *
# It pollutes your namespace and makes code harder to understand.

# Aliases are useful for long module names:
import datetime
print("Today:", datetime.date.today())

# You can also alias specific names:
from math import factorial as fact
print("6! =", fact(6))

# Good practice:
# - import math              -> clear where names come from
# - from math import pi      -> fine for a few well-known names
# - import numpy as np       -> follow community conventions
