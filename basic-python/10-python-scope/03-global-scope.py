# Global Scope
# A variable created at the top level of a file is global.
# It can be read from anywhere: inside functions, loops, conditions.

player_name = "Aryan"     # global variable
high_score = 1000         # global variable

def show_player():
    # Reading a global variable inside a function works fine
    print("Player:", player_name)
    print("High score:", high_score)

show_player()

# Global variables are shared: everyone sees the same value
def show_again():
    print("Still the same player:", player_name)

show_again()

# ⚠️ But be careful: reading is easy, writing is tricky.
# If you try to CHANGE a global variable inside a function
# without declaring it, Python creates a NEW local variable
# with the same name instead (see the next file for the fix).

def try_to_change():
    player_name = "Priya"   # this creates a LOCAL variable, not a change!
    print("Inside function:", player_name)

try_to_change()
print("Outside function:", player_name)   # still "Aryan"
