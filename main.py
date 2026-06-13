from game import get_secret_number
from game import check_guess


secret_number = get_secret_number()

while True:

    guess = int(input("Enter a number between 1, and 10: "))

    result = check_guess(secret_number, guess)

    print(result)

    if result == "Correct!":
        break