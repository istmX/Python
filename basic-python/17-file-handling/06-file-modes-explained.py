# File Modes Explained
# The second argument to open() controls what you can do.

# "r"  -> read (default). File must exist.
# "w"  -> write. Erases the file or creates it.
# "a"  -> append. Adds to the end of the file.
# "x"  -> create. Fails if the file already exists.
# "r+" -> read and write. File must exist.
# "b"  -> binary mode (e.g., "rb", "wb") for non-text files

# --- "r" : read ---
with open("modes_demo.txt", "w") as file:
    file.write("original\n")

with open("modes_demo.txt", "r") as file:
    print("r mode:", file.read())

# --- "w" : write (erases!) ---
with open("modes_demo.txt", "w") as file:
    file.write("replaced\n")

with open("modes_demo.txt", "r") as file:
    print("w mode:", file.read())

# --- "a" : append ---
with open("modes_demo.txt", "a") as file:
    file.write("appended\n")

with open("modes_demo.txt", "r") as file:
    print("a mode:", file.read())

# --- "x" : create (fails if exists) ---
import os
if os.path.exists("fresh_file.txt"):
    os.remove("fresh_file.txt")

with open("fresh_file.txt", "x") as file:
    file.write("created fresh\n")

# with open("fresh_file.txt", "x") as file:   # would raise FileExistsError
#     pass

# --- "r+" : read and write ---
with open("modes_demo.txt", "r+") as file:
    content = file.read()
    file.seek(0)
    file.write("R+" + content)

with open("modes_demo.txt", "r") as file:
    print("r+ mode first line:", file.readline().strip())

# Rule of thumb: use "r" to read, "w" to overwrite, "a" to append,
# and always wrap your code in 'with'.
