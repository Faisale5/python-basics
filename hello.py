name = input("What's your name? ")
age = int(input("how old are you? "))
City = input("What city do you live in?")
experience = int(input("How many years have you been learning IT?"))

years = 65 - age
remaining = 10 - experience

print()
print(f"Welcome, {name}!")
print(f"You have about {years} years until you're 65.")
print(f"You live in {City}.")
print(f"In about {remaining} more years of learning and experience, you could be aiming for senior IT roles.")
print("Keep Learning every day")
