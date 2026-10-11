for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#brake 
name = input("Enter your name: ")

for ch in name:
    if ch == " ":
        continue
    print(ch)

print("Done")
