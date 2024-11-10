# Checking the data type of a boolean value
print(type(True))  # Outputs: <class 'bool'>

# Comparing uppercase and lowercase letters
print("H" > "h")  # False, since lowercase letters have higher ASCII values than uppercase
print(ord("H"))  # Value of 'H' (72)
print(ord("h"))  # Value of 'h' (104)

# Initializing two integer variables
a = 10
b = 110

# Performing various comparison operations between a and b
print(a > b)   # False, 10 is not greater than 110
print(a < b)   # True, 10 is less than 110
print(a >= b)  # False, 10 is not greater than or equal to 110
print(a <= b)  # True, 10 is less than or equal to 110
print(a == b)  # False, 10 is not equal to 110
print(a != b)  # True, 10 is not equal to 110

# Performing more comparison operations
x = 1
y = 2
c = 3
print(x > 1)         # False, since x is not greater than 1
print(not x > 1)     # True, the result of x > 1 is negated with 'not'
print(y > 1)         # True, y is greater than 1

# Demonstrating the logical operators 'and', 'or', 'not'
x = 1
y = 2
c = 3
print(x > 1 and y > 1)       # False, x > 1 is False but y > 1 is True
print(x > 1 or y > 1 or c > 2)  # True, at least one condition is True (c > 2)

# Logical operations with boolean values
print(True and True)     # True, both values are True
print(True or True)      # True, at least one value is True
print(not True)          # False, negating True

print(False and False)   # False, both values are False
print(False or False)    # False, no True values
print(not False)         # True, negating False

print(True and False)    # False, one value is False
print(True or False)     # True, at least one value is True

# Defining variables for personal information
name = "Joe"
age = 45
is_married = False

# Using conditional statements to print different messages
if age > 18 and age < 39 and is_married == False:
    print("Hi {}! Congratulations".format(name))  # Prints if age is between 18 and 39 and not married
if age >= 40 and is_married == False:
    print("Ti dovboyob")  # Prints if age is 40 or above and not married

# Checking equality in a conditional statement
x = 3
print(x == 3)  # True, as x is indeed equal to 3

# Taking user input and checking conditions
user_input = int(input("Enter any number"))
if user_input >= 0 and user_input != 7:
    print('Thank you! Have a nice day!')  # Prints if the input is non-negative and not 7
elif user_input == 7:
    print("'7 is a lucky number! Today is your lucky day!'")  # Special message if input is 7

# Taking another user input to check if it is even or odd
user_input = int(input('Enter an integer number'))
if user_input % 2 == 0:
    print('The number is even') 
elif user_input % 2 != 0:
    print('The number is odd') 
