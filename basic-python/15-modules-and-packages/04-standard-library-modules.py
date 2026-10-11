# Standard Library Modules You Should Know
# Python ships with hundreds of useful modules. No installation needed!

# --- math: mathematical functions ---
import math
print("Ceiling of 4.2:", math.ceil(4.2))      # 5
print("Floor of 4.8:", math.floor(4.8))       # 4
print("Power 2^10:", math.pow(2, 10))         # 1024.0

# --- random: random numbers and choices ---
import random
print("Random float (0-1):", random.random())
print("Shuffle:", random.sample(range(1, 11), 5))

# --- datetime: dates and times ---
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print("Today:", today)
print("Year:", today.year, "Month:", today.month, "Day:", today.day)
print("Now:", now.strftime("%H:%M:%S"))

# --- os: interact with the operating system ---
import os
print("Current working directory:", os.getcwd())
print("Files in current folder:", os.listdir("."))

# --- sys: system-specific information ---
import sys
print("Python version:", sys.version.split()[0])
print("Platform:", sys.platform)

# Explore more with: help("modules") in a Python shell
