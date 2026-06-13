import random

print("Welcome to Guess The Number")

secret_number = random.randint(1, 10)

guess = int(input("Enter a number between 1 and 10: "))

if guess == secret_number:
    print("Correct!")

elif guess < secret_number:
    print("Too low!")

else:
    print("Too high!")