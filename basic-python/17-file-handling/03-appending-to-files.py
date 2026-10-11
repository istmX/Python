# Appending to Files
# Use mode "a" to ADD content at the end without erasing.

# Start fresh
with open("log.txt", "w") as file:
    file.write("Program started.\n")

# Append new entries — old content stays
with open("log.txt", "a") as file:
    file.write("User logged in.\n")

with open("log.txt", "a") as file:
    file.write("Data saved.\n")

with open("log.txt", "r") as file:
    print("Log content:")
    print(file.read())

# Appending is perfect for logs, records, and history files
# because nothing is ever erased.

# Append in a loop
with open("count_log.txt", "w") as file:
    file.write("Counting:\n")

for number in range(1, 6):
    with open("count_log.txt", "a") as file:
        file.write(f"Count: {number}\n")

with open("count_log.txt", "r") as file:
    print(file.read())
