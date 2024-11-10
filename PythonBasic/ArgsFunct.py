# args and key word args

def ten_percent_of_num(a, b, c):
    # This function takes three numbers, multiplies them together, and returns 10% of the result
    return (a * b * c) * 0.1

print(ten_percent_of_num(10, 20, 5)) 

# Using *args to handle an unknown number of positional arguments

def ten_percent_of_num_args(*args):
    # This function calculates 10% of the product of all numbers passed in
    basic_item = 1  # Starting point for multiplication
    for num in args:
        basic_item = basic_item * num  # Multiply each argument into basic_item
    return basic_item * 0.1  # Return 10% of the final product

print(ten_percent_of_num_args(10, 10, 10))  # Outputs 10% of 10 * 10 * 10, which is 10

# Using **kwargs to handle keyword arguments

def func_with_kwargs(**kwargs):
    # This function simply prints the dictionary created by keyword arguments
    print(kwargs)  # kwargs will contain {'fnum': 1, 'snum': 2, 'tnum': 3}

func_with_kwargs(fnum=1, snum=2, tnum=3)  # Outputs the dictionary of keyword arguments


# Using **kwargs to add optional details in a function

def greeting_with_kwargs(greeting, **kwargs):
    # This function greets the user; if a name is given in kwargs, it includes the name in the greeting
    if "name" in kwargs:
        print("{}! Nice to meet you, {}".format(greeting, kwargs["name"]))  # Prints greeting with name
    else:
        print("{}! What is your name?".format(greeting))  # Prompts for name if none is given

greeting_with_kwargs(greeting="Hi there", name="John")  # Outputs: "Hi there! Nice to meet you, John"


# Combining *args and **kwargs to handle both positional and keyword arguments

def func_with_args_and_kwargs(*args, **kwargs):
    # This function prints positional arguments as a tuple and keyword arguments as a dictionary
    print(args)  # Outputs positional arguments as a tuple
    print(kwargs)  # Outputs keyword arguments as a dictionary

func_with_args_and_kwargs("one", "two", drink="cha", food="pizza")

# with args - when you don't know the amount of numbers 
def ten_percent_of_num_args(*args):
    basic_item = 1
    for num in args:
        basic_item = basic_item * num
    return basic_item * 0.1

print(ten_percent_of_num_args(10, 10, 10))

# **kwargs
def func_with_kwargs(**kwargs):
    print(kwargs)

func_with_kwargs(fnum = 1, snum = 2, tnum = 3)

def greeting_with_kwargs(greeting, **kwargs):
    if "name" in kwargs:
        print("{}! Nice to meet you, {}".format(greeting, kwargs["name"]))
    else:
        print("{}! what is your name?".format(greeting(str)))
              
greeting_with_kwargs(greeting="Hi there", name="John")

# args + kwargs
def func_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

func_with_args_and_kwargs("one", "two", drink="cha", food="pizza")