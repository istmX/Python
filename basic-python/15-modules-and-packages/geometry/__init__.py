# geometry package
# A small package that groups geometry-related modules together.

# Packages usually contain an __init__.py file.
# It runs when the package is first imported and can be used
# to expose commonly used names.

PI = 3.14159

# These imports make the submodules available as
# geometry.circle and geometry.rectangle
from . import circle
from . import rectangle
