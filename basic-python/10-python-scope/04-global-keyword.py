# The global Keyword
# To change a global variable from inside a function,
# tell Python explicitly: "this name refers to the global variable."

score = 0          # global variable

def increase_score():
    global score   # declare that we mean the global 'score'
    score = score + 10
    print("Score inside function:", score)

increase_score()   # Score inside function: 10
increase_score()   # Score inside function: 20
print("Score outside function:", score)   # 20 (the global was changed)

# Without 'global', the line score = score + 10 would fail,
# because Python would treat score as a local variable that
# has not been assigned yet.

# ⚠️ Good practice:
# Using global variables inside functions can make code hard to follow.
# Prefer passing values as parameters and returning results instead.

def better_increase(current_score):
    return current_score + 10

score = better_increase(score)
print("Better approach:", score)   # 30
