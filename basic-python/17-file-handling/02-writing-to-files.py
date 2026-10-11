# Writing to Files
# Use mode "w" to write. WARNING: "w" ERASES existing content!

# Write (creates the file if it does not exist)
with open("output.txt", "w") as file:
    file.write("First line\n")
    file.write("Second line\n")

# Read it back to confirm
with open("output.txt", "r") as file:
    print(file.read())

# Writing again ERASES the old content
with open("output.txt", "w") as file:
    file.write("Brand new content.\n")

with open("output.txt", "r") as file:
    print("After rewrite:")
    print(file.read())

# write() only accepts strings — convert numbers first
with open("numbers.txt", "w") as file:
    file.write(str(42) + "\n")
    file.write(str(3.14) + "\n")

# writelines() writes a list of strings (you add the newlines)
with open("numbers.txt", "w") as file:
    file.writelines(["10\n", "20\n", "30\n"])

with open("numbers.txt", "r") as file:
    print("numbers.txt:", file.read())
