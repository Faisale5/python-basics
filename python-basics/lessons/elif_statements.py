age = int(input("What is your age?"))
name = input("What is your name?")

print(f"Welcome {name}!")
if age < 13:
    print("You are a child.")

elif age < 18:
    print("You are a teenager")

else:
    print("You are an adult")

