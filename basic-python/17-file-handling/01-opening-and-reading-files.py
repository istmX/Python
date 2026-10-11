# Opening and Reading Files
# The open() function returns a file object.
# Always close files when done (or use 'with' — see file 04).

# Step 1: create a file to read (so this example is self-contained)
with open("demo_notes.txt", "w") as file:
    file.write("Python is fun.\n")
    file.write("Files let programs remember data.\n")

# Step 2: open the file for reading
file = open("demo_notes.txt", "r")

# read() returns the ENTIRE file content as one string
content = file.read()
print("Full content:")
print(content)

# Done reading — close the file
file.close()

# After reading, the file object is "exhausted":
# reading again returns an empty string.
file = open("demo_notes.txt", "r")
file.read()          # read everything
print("Second read (empty):", repr(file.read()))   # ''
file.close()

# To read again, reopen the file or use seek(0) to rewind.
file = open("demo_notes.txt", "r")
file.read()
file.seek(0)         # rewind to the beginning
print("After seek(0):", file.read())
file.close()
