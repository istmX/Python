print("Guess the number")

score = 0

while True:
    i = int(input("enter a random value between 1 and 100: "))
    score = score + 1

    if i == 42:
        print("you guessed it")
        print("score:", score)
        break
    else:
        print("try again")
