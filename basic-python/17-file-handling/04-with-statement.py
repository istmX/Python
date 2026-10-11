# The with Statement (Context Manager)
# 'with' automatically closes the file when the block ends —
# even if an error happens. This is the recommended way.

# Without with (easy to forget closing)
file = open("with_demo.txt", "w")
file.write("Hello\n")
file.close()        # must remember!

# With with (automatic and safe)
with open("with_demo.txt", "w") as file:
    file.write("Hello from with!\n")
# file is already closed here — no need for file.close()

# Reading with with
with open("with_demo.txt", "r") as file:
    print(file.read())

# The file is guaranteed to be closed, even if read() fails:
with open("with_demo.txt", "r") as file:
    content = file.read()
    # something_undefined   # even if this raised an error...
# ...the file would still be closed.

# You can open multiple files at once:
with open("with_demo.txt", "r") as source, open("with_copy.txt", "w") as target:
    target.write(source.read())

with open("with_copy.txt", "r") as file:
    print("Copy content:", file.read())
