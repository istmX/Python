# Mini Project: Word Frequency Counter
# This project uses comprehensions to analyze text.

sentence = "the quick brown fox jumps over the lazy dog the fox is quick"

print("=" * 45)
print("WORD FREQUENCY COUNTER")
print("=" * 45)

# Split the sentence into words
words = sentence.split()
print("Words:", words)

# 1. Build a dictionary of word frequencies using a comprehension
#    (count each word with words.count — fine for small texts)
unique_words = set(words)
frequency = {word: words.count(word) for word in unique_words}

print("\n--- Word frequencies ---")
for word, count in frequency.items():
    print(f"{word}: {count}")

# 2. Find words that appear more than once (with a condition)
repeated = {word: count for word, count in frequency.items() if count > 1}
print("\n--- Repeated words ---")
print(repeated)

# 3. Sort words by length using a comprehension + sorted
by_length = sorted(words, key=len)
print("\n--- Words sorted by length ---")
print(by_length)

# 4. Build a set of words starting with a specific letter
letter = "f"
f_words = {word for word in words if word.startswith(letter)}
print(f"\n--- Words starting with '{letter}' ---")
print(f_words)

# 5. Create a "length map": each unique word -> its length
length_map = {word: len(word) for word in unique_words}
print("\n--- Word lengths ---")
print(length_map)

print("\n" + "=" * 45)
