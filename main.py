print("Welcome to Guess The Number")

secret_number = 7

guess = int(input("Enter a number: "))

if guess == secret_number:
    print("Correct!")
else:
    print("Wrong!")