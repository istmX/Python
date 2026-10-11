# Mini Project: Generator Toolbox
# This project demonstrates generators with three practical tools:
# a Fibonacci generator, a custom range generator,
# and a file reader that processes large files safely.

def fibonacci(limit):
    """Yield the first 'limit' Fibonacci numbers."""
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count = count + 1


def custom_range(start, end, step=1):
    """Like range(), but written as a generator (for learning)."""
    current = start
    while current < end:
        yield current
        current = current + step


def read_file_in_chunks(filename, chunk_size=2):
    """Yield a file's content 'chunk_size' lines at a time.

    This keeps memory usage low even for very large files.
    """
    try:
        with open(filename, "r") as file:
            chunk = []
            for line in file:
                chunk.append(line)
                if len(chunk) == chunk_size:
                    yield chunk
                    chunk = []
            if chunk:                # yield the remaining lines
                yield chunk
    except FileNotFoundError:
        yield f"File '{filename}' not found."


# ---- Tool 1: Fibonacci ----
print("--- Fibonacci (first 10) ---")
for number in fibonacci(10):
    print(number, end=" ")
print()

# ---- Tool 2: Custom range ----
print("\n--- Custom range (2 to 10, step 2) ---")
for number in custom_range(2, 10, 2):
    print(number, end=" ")
print()

# ---- Tool 3: File chunk reader ----
print("\n--- File chunk reader ---")
# Create a sample file first
with open("big_sample.txt", "w") as file:
    for i in range(1, 8):
        file.write(f"Line {i}\n")

for chunk in read_file_in_chunks("big_sample.txt", chunk_size=3):
    print("Chunk:", [line.strip() for line in chunk])

# Missing file handling
print("\n--- Missing file ---")
for chunk in read_file_in_chunks("missing.txt"):
    print(chunk)
