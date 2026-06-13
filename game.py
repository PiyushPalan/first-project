import random

def get_secret_number():
    return random.randint(1, 10)

def check_guess(secret, guess):

    if guess < secret:
        return "Too low!"

    elif guess > secret:
        return "Too high!"

    else:
        return "Correct!"