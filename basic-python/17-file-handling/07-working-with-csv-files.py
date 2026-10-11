# Working with CSV Files
# CSV (Comma Separated Values) is a simple format for tables.
# Python's csv module makes reading and writing CSV easy.

import csv

# --- Writing CSV data ---
students = [
    ["Name", "Math", "Science", "English"],
    ["Aryan", "88", "92", "79"],
    ["Priya", "95", "91", "97"],
    ["Rahul", "60", "72", "65"],
]

with open("marks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("marks.csv created.")

# --- Reading CSV data ---
print("\n--- Reading the CSV file ---")
with open("marks.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)          # each row is a list of strings

# --- Reading into dictionaries ---
print("\n--- As dictionaries ---")
with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # each row is a dictionary: {"Name": "Aryan", "Math": "88", ...}
        average = (int(row["Math"]) + int(row["Science"]) + int(row["English"])) / 3
        print(f"{row['Name']}: average {average:.1f}")

# CSV is the standard format for spreadsheets and data exchange.
# Files created by Excel open perfectly with the csv module.
