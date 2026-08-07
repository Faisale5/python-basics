try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("That is not a valid number!")

try:
    age = int(input("How old are you? "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid age.")
