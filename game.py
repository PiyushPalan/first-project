import random


def get_secret_number():
    return random.randint(1, 10)


def check_guess(secret_number, guess):

    if guess < secret_number:
        return "Too low!"

    elif guess > secret_number:
        return "Too high!"

    else:
        return "Correct!"