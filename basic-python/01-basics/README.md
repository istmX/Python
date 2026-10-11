# Python Basics 🐍

This folder introduces the **absolute basics of Python** that every beginner must understand before moving to conditions, loops, and logic.

The goal here is not speed.  
The goal is **clarity**.

If you understand this folder well, Python will stop feeling confusing.

---

## 🧠 Why This Folder Exists

If you are coming from languages like **C or C++**, Python may feel strange at first because:

- no `main()` function
- no semicolons `;`
- no data type declaration before variables
- code looks very simple (but it is powerful)

Python focuses on **readability** and **doing more with less code**.

This folder helps you adjust your thinking to Python’s style.

---

## 🖥️ Input and Output (`input_output.py`)

### Why Input and Output Matter

Programs are useless if they:
- cannot take data from users
- cannot show results

Python uses:
- `input()` → to take data from the user
- `print()` → to show output on the screen

---

### Example Idea

```python
name = input("Enter your name: ")
print("Hello", name)
What happens:

Python waits for the user to type something

Stores it in a variable

Prints a message using that data

💡 Important note:
input() always returns text (string), even if the user types a number.

📦 Variables (variables.py)
What Is a Variable?

A variable is like a box that stores information.

Example:

city = "Delhi"
age = 18


Here:

city stores text

age stores a number

In Python:

you do NOT need to declare data types

Python decides automatically

This is different from C/C++ and makes Python easier for beginners.

🧵 Strings (strings.py)
What Is a String?

A string is text.

Anything written inside quotes is a string.

Examples:

"Hello"

'Python'

"My name is Aryan"

Strings are used for:

user input

messages

output

interaction with users

Creating Strings
name = "Python"
message = 'Hello World'


Both single and double quotes work.

Useful String Operations
name.upper()   # converts to uppercase
name.lower()   # converts to lowercase
len(name)      # counts characters


These do NOT change the original string.
They return a new value.

🚪 Escape Sequences (escape_sequences.py)

Escape sequences help format output.

They start with a backslash (\).

Common Escape Sequences

\n → new line

\t → tab space

\" → double quote

\' → single quote

\\ → backslash

Example:

print("Name:\tAge")
print("Hello\nWorld")


Escape sequences are mostly used with print() to make output readable.

🔄 Type Conversion (type_conversion.py)
Why Type Conversion Is Needed

input() always gives a string.

So this will cause an error:

age = input("Enter age: ")
print(age + 1)


Because Python cannot add a number to text.

Correct Way
age = int(input("Enter age: "))
print(age + 1)


💡 Important shortcut explained:

int(input())


This means:

take input

immediately convert it to integer

store the result

This is very common in Python and totally safe when used correctly.

🧪 Mini Projects (Practice Files)
📄 Simple Profile Creator

This project:

takes name, city, and hobby

prints a formatted profile

What it teaches:

input

variables

strings

escape sequences

clean output formatting

This is how real programs start — small and simple.

📄 Age Calculator
name = input("Enter your name: ")
year = int(input("Enter birth year: "))

age = 2025 - year
print("Hello", name)
print("You are", age, "years old")


What it teaches:

type conversion

basic logic

real-world calculation

clean user interaction

This is a perfect beginner project.

📂 Files in This Folder

01-input_output.py → taking input and showing output

02-strings.py → working with text

03-variables.py → storing data

04-comments.py → adding notes to code

05-common_errors.py → mistakes every beginner makes

06-execution_flow.py → how Python reads code

07-naming_rules.py → how to name variables

08-print_formatting.py → formatting output with print()

09-type_conversion.py → converting input values

10-python_keywords.py → words Python reserves

11-mini_project.py → age calculator mini project

12-project-simple-profile.py → simple profile creator mini project

🧠 Beginner Advice (Read This)

If something breaks:

don’t panic

read the error

check spelling

check indentation

check quotes

Python errors are not insults.
They are instructions.

📌 Final Note

This folder trains your thinking, not just syntax.

If you understand this folder properly:

conditions will feel easy

loops will make sense

projects won’t scare you

Don’t rush.
Strong basics build strong developers.




## 📬 Contact

For questions or feedback, open an issue on GitHub:
https://github.com/istmX/Python

---

© 2026 ISTMX. All rights reserved.

ISTMX — Python Learning Resource  
Aryan — Developer & Maintainer




