Lesson 1 - Python Basics
Python is a programming language used to create:
- Websites
- Games
- Apps
- Cybersecurity tools
- AI
- Automation scripts

Print() - Used to display information
  Example: 
   in python: print("Hello World")
   Output: Hello World

Variables - Store information.
 Example:
 in python: name = "Faisal"
            age = 22
    think of a variable as a labelled box that stores data

User Input
 Use input() to ask the user a question
 Example:
 name = input(What is your name? ")

Data Types
String (text)
 name = "Faisal"

Integer (whole number)
 age = 22

Convert input into an integer:
 age = int(input("Age: "))

f-Strings
 Used to insert variables into text.
 Instead of:
  print("hello", name)
 Use:
  print(f"Hello {name}!")

Comparison Operators
 Used to compare values
  == Equal to
  != Not equal to
  > Greater than
  < Less than
  >= Greater than or equal to
  <= Less than or equal to
   Example:
   Python: age >= 18
   Returns:
           True
    or
           False
used to:
- check if a user can log in.
- check if someone is old enough
- check exam scores
- validate passwords
- build games
- build websites
- create cybersecurity tools

if Statement
 Runs code only if the condition is True.
 python:
 if age >= 18:
        print("Adult")

else Statement
 Runs when the condition is False.
 Example:
  Python:
  if age >= 18:
     print("Adult")
  else:
     print("Under 18")

elif Statement
 Checks another condition
 Example:
  Python:
  if age < 13:
     print("child")
  elif age < 18:
      print("Teenager")
  else:
      print("Adult")

and Operator
 Both conditions must be True.
 Example:
  Python:
  if username == "faisale5" and password == "python123":
       print("Access Granted")
else:
       print("Access Denied")

Indentation
 Python uses indentation (4 spaces) to know what code belongs together.
  Correct:
  if age >= 18:
       print("Adult")
  Wrong:
  if age >= 18:
  print("Adult")

Logical Operators
 Logical Operators combine conditions.

Logical operators are used everywhere:
- Login systems
- Online stores
- Games
- Websites
- Cybersecurity tools

 ### and Operator
  Both conditions must be true.
  Example:
  if username == "admin" and password == "python123":

  or Operator
  At least one condition must be True.
  Example:
  if age < 18 or age > 65:

  not Operator
  Reverses a True or False value.
  Example:
  logged_in = False
  print(not logged_in)
  output = true

## While Loops
A while loop repeats code while a condition is true.
Syntax:
python
number = 1 

while number <= 10:
   print(number)
   number = number + 1
the loop stops when the condition becomes false.
Remember:
 while reppeats code.
 Update the variables inside the loop.
 If you don't update it, you can create an infinite loop.

## for Loops
 for loops repeat code a specific number of times.
 Syntax:
 for variable in range(start, stop):
      print(variable)
 Remember:
 range(1, 6) prints 1 to 5.
 The stop number is not included.
 Use a negative step (-1) to count backwards.
 
## Strings
 A string is text.
   name = "Faisal"
 Useful functions:
  len(name)  # Length
  name.upper() # Uppercase
  name.lower() # Lowercase
 Access characters:
  name[0] # First letter
  name[1] # Second letter
  name[-1] # Last letter



  
What I Built:
- Hello World
- Personal Information Program
- if Statement Program
- Login Program
- elif Statement Program
- Comparison Operators Program

