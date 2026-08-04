# or Operator means at least one condition must be true
#Example:
age = int(input("How old are you? "))
if age < 13 or age >+65:
    print("You get a discount!")
else:
    print("No discount.")

# not Operator reverses a True/False value.
#Example:
logged_in = False
print(not logged_in)

#Challenge:
ages = int(input("How old are you?"))
if ages < 18 or age > 65:
    print("Special pricing applies.")
else:
    print("Standard pricing.")
    