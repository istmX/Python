# Reading Files Line by Line
# Files are iterable — you can loop over them directly.
# This is memory-friendly even for large files.

# Prepare a file to read
with open("students.txt", "w") as file:
    file.write("Aryan - 88\n")
    file.write("Priya - 95\n")
    file.write("Rahul - 72\n")

# Method 1: loop over the file object directly (recommended)
print("--- Method 1: direct loop ---")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())   # strip() removes the newline

# Method 2: readline() reads one line at a time
print("\n--- Method 2: readline() ---")
with open("students.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# Method 3: readlines() returns a list of all lines
print("\n--- Method 3: readlines() ---")
with open("students.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Practical example: count students and total marks
total = 0
count = 0
with open("students.txt", "r") as file:
    for line in file:
        parts = line.split("-")
        marks = int(parts[1])
        total = total + marks
        count = count + 1

print(f"\nStudents: {count}, Total marks: {total}, Average: {total / count}")
