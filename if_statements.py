age = int(input("How old are you? "))
password = input("What is your password?")

if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

