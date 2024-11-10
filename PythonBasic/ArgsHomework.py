# 1. Check if "cat" is among the provided arguments

def is_cat_here(*args):
    # This function checks if the string "cat" (case-insensitive) is in the arguments
    return any(arg.lower() == "cat" for arg in args)  # Converts each argument to lowercase and checks if any equals "cat"

print(is_cat_here("dog", "hippo", "cat"))  # True, as "cat" is one of the arguments


# 2. Check if a specific item is among the provided arguments

def is_item_here(item, *args):
    # This function checks if the item is in the list of arguments
    return item in args  # Returns True if item matches any of the arguments exactly

# Test cases for the is_item_here function
print(is_item_here("dog", "dog", "cat"))        # True, "dog" is in the arguments
print(is_item_here("dog", "hippo", "cat"))      # False, "dog" is not in the arguments
print(is_item_here("dog", "Dog", "cat"))        # False, "dog" does not match "Dog" due to case sensitivity
print(is_item_here("dog", "racoon", "dog", "cat"))  # True, "dog" is in the arguments multiple times


# 3. Print a favorite color with an optional secondary color if provided

def your_favorite_color(my_color, **kwargs):
    # This function accepts a favorite color and optionally another color in kwargs
    if "color" in kwargs.keys():
        # If "color" is in kwargs, print a message that includes both colors
        print("My favorite color is " + my_color + " but " + kwargs["color"] + " is also pretty good!")
    else:
        # If no additional color is provided, prompt the user to share their favorite color
        print("My favorite color is " + my_color + ". What is your favorite color?")

your_favorite_color("blue", color="green")  # "My favorite color is blue but green is also pretty good!"


# V2: Same function, using format() for string formatting

def your_favorite_color(my_color, **kwargs):
    # This function also checks for an additional color in kwargs and formats the output using format()
    if 'color' in kwargs.keys():
        # If "color" is in kwargs, print both colors using format()
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        # If no additional color is provided, prompt for a favorite color using format()
        print('My favorite color is {}, what is your favorite color?'.format(my_color))

your_favorite_color("blue", color="green")  # Output will be the same as above
