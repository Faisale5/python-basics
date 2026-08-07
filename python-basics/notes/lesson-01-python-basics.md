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

## Lists
 A list stores multiplevalues in one variable.
 Example:
 fruits = ["Apple", "Banana", "Orange"]

 Access items:
 fruits[0] # Apple
 fruits[1] # Banana
 fruits[-1] # Orange

 Useful methods:
 append() -> Adds an item to the end.
 remove() -> Removes an item by value.
 len() -> Returns the number of items.

 Lists are mutable, meaning they can be changed after they are created.

 ## Functions
  A function is a reusable block of code.
  Create a function:
  def greet():
    print("Hello!")

 Run a function:
 greet()

 Remember:
 - def creates a function.
 - The function does nothing until you call it.
 - Functions reduce repeated code.

## Functions with Parameters
A parameter lets you pass information into a function.
Example:

def greet(name):
    print(f"Hello {name}!")
 Call the function:
 greet("Faisal")
 greet("Omar")
 greet("Ali")

 Output:
 Hello Faisal!
 Hello Omar!
 Hello Ali!

 Remember
 - Parameters are variables inside the function.
 - Arguments are the values you pass when calling the function.

 Multiple Parameters
  Functions can have more than one parameter.
  Example:
  def person(name, age):
   print(f"{name} is {age} years old.")
   Calling it:
   person("Faisal", 22)
   Output:
   Faisal is 22 years old.
 
  Return
   Return sends a value back from the function.
   Example:
   def add(a, b):
    return a + b
   results = add(15, 10)
   print(results)
   Output:
   25

 print() vs return
 using print():
 def add(a, b):
 print(a + b)
 displays the answer but doesn't save it.
 using return:
 def add(a, b):
 return a + b
 Returns the answer so it can be stored in a variable.
 Example:
 result = add(5, 5)
 Now result contains:
 10
 
 Variable Scope
 Global Variable
 Created outside a function.
 Example:
 def greet():
   print(name)
 greet()
  Output: Faisal
 Global variables can usually be accessed from inside functions.

 Local Variable
 Created inside a function.
 Example:
 def greet():
  name = "Faisal"
  print(name)
 greet()
 print(name)
 Output:
 Faisal
 NameError: name 'name' is not defined
 The variable only exists while the function is running.
 
 Local vs Global
 name = "Faisal"
 def greet():
 name = "Omar"
 print(name)
 greet()
 print(name)
 Output:
 Omar
 Faisal
 The local variable does not change the global variable.

 Remember:
  - def creates a function.
  - A function does nothing until it is called.
  - Parameters allow functions to accept information.
  - Arguments are the values passed into parameters.
  - return sends a value back.
  - Local variables only exist inside their function.
  - Global variables are created outside functions.

  Study tip:
  - def -> Create the function.
  - () -> Call the function.
  - Parameters -> Receive information
  - return -> Give back information.

## Dictionaries
 A dictionary stores data as key: value pairs.
 Example:
 person = {
   "name": "Faisal",
   "age": 22
 }
 Keys must be unique.

 Access a value
 print(person["name"])
 Output: Faisal

 Update a value
 person["age"] = 23
 
 Add a new key
 person["country"] = "Australia"

 Delete a key
 del person["country"]
 
 Print the whole dictionary
 print(person)
 Output:
 {'name': 'Faisal', 'age': 23}

 Dictionary Rules
 - Uses {}
 - Stores key : values pairs
 - Access values using keys
 - Keys must be unique
 - Values can be strings, integers, booleans, floats, lists, or even other dictionaries

 ## Tuples
 A tuple stores multiple values like a list, but cannot be changed.
 months = ("January", "February", "March")

 Access items
 months[0]
 months[1]
 months[-1]

 Tuple Rules:
 - Uses ()
 - Ordered
 - Indexed
 - Immutable (cannot chang)
 - Faster than lists
 - Good for data that should never change

## Sets
 A set stores unique values.
 fruits = {"apple", "banana", "orange"}

 Add an item:
 fruits.add("mango")
 
 Remove an item:
 fruits.remove("banana")

 Rules:
 - Uses {}
 - Unordered
 - No indexes
 - No duplicates
 - Changeable( add/remove items)

## Error Handling
 try lets Python attempt to run some code.
 except tells python what to do if an error occurs.

 Example:
 try:
    number = int(input("Enter a number: "))
    print(number)
 except ValueError:
    print("That is not a valid number!")

 Why use it?
 - Prevents your program from crashing.
 - Gives the user a helpful message.
 - Makes programs more reliable.



What I Built:
- Hello World
- Personal Information Program
- if Statement Program
- Login Program
- elif Statement Program
- Comparison Operators Program

