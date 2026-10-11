# What Are Packages?
# A package is a folder that contains multiple modules.
# Packages help organize large projects.
#
# A package folder usually contains an __init__.py file
# (it can be empty) that tells Python: "this folder is a package".
#
# Example structure:
#   my_project/
#   ├── main.py
#   └── geometry/              <- package
#       ├── __init__.py
#       ├── circle.py           <- module
#       └── rectangle.py        <- module

# This topic folder contains a real package called "geometry".
# Let's import from it:

from geometry.circle import area as circle_area
from geometry.rectangle import area as rectangle_area

print("Circle area (r=5):", round(circle_area(5), 2))
print("Rectangle area (4x6):", rectangle_area(4, 6))

# You can also import the package's __init__ exports directly:
import geometry
print("Pi used by the package:", geometry.PI)

# Import styles compared:
#   from geometry.circle import area      -> import one function
#   from geometry import circle           -> import a module from a package
#   import geometry.circle as circ        -> import with an alias
