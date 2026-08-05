secret = 7
number = int(input("Guess the number "))



while number != secret:
    print("Wrong! Try again.")
    number = int(input("Guess again: "))

print("Congratulations! You guessed it!")


