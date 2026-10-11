# try / except / else / finally
# The complete exception-handling structure.

# try     -> risky code
# except  -> runs if an exception happens
# else    -> runs if NO exception happened
# finally -> ALWAYS runs (with or without an error)

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        print("Division succeeded.")
        return result
    finally:
        print("This always runs (cleanup could go here).")

print("--- Valid division ---")
print("Result:", divide(10, 2))

print("\n--- Division by zero ---")
print("Result:", divide(10, 0))

# finally is perfect for cleanup tasks:
# closing files, releasing resources, printing status messages.
# It runs even if you return from inside try or except.

# A practical file example:
try:
    file = open("nonexistent_file.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print("File read successfully, length:", len(content))
finally:
    # close the file only if it was opened
    print("File handling finished.")
