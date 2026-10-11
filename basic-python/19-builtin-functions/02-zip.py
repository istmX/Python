# zip() — Combine Lists Pair by Pair
# zip() takes multiple iterables and pairs their items together.

names = ["Aryan", "Priya", "Rahul"]
marks = [88, 95, 72]

# Pair each name with its mark
for name, mark in zip(names, marks):
    print(f"{name}: {mark}")

# zip() stops at the SHORTEST iterable
short_names = ["A", "B"]
long_marks = [1, 2, 3, 4]
print(list(zip(short_names, long_marks)))   # only 2 pairs

# Build a dictionary directly with zip()
scoreboard = dict(zip(names, marks))
print("Scoreboard:", scoreboard)

# Unzip: zip(*paired) separates them back
paired = [("x", 1), ("y", 2), ("z", 3)]
letters, numbers = zip(*paired)
print("Letters:", letters)
print("Numbers:", numbers)

# zip() is great for walking through two lists in lockstep:
subjects = ["Math", "Science", "English"]
for subject, mark in zip(subjects, marks):
    print(f"{subject}: {mark}")
