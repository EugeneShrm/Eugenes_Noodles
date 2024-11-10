#1
def cat_voice():
    print("Meow")

cat_voice()

def dog_voice():
    print("Woof")

dog_voice()

#2
def cat_voice(str):
    return "Meow"

print(cat_voice(str))

def dog_voice(str):
    return "Woof"

print(dog_voice(str), dog_voice(str))

#3
# Define a function that appends "!" to the input text

def get_voice(text):
    '''
    :param text: A string to which an exclamation mark will be added
    :return: The input text with "!" appended to the end
    '''
    return text + "!"  # Adds an exclamation mark to the text and returns it

# Call the get_voice function and print the result
return_value = get_voice("Hello")
print(return_value)  # Outputs: "Hello!"


# Define a function to generate a list of odd numbers within a given range

def odd_numbers_range(a, b):
    # This function uses a list comprehension to return a list of odd numbers from a to b-1
    return [num for num in range(a, b) if num % 2 != 0]  # Only numbers that aren't divisible by 2 are included

print(odd_numbers_range(2, 20))  # Outputs a list of odd numbers between 2 and 20


# Define a function that generates and prints a list of odd numbers in a range

def generator(a, b):
    # This function initializes an empty list and populates it with odd numbers from a to b-1
    some_list = []  # Initialize an empty list to hold odd numbers
    for num in range(a, b):
        if num % 2 != 0:  # Check if the number is odd
            some_list.append(num)  # Add the odd number to the list
    print(some_list)  # Print the list of odd numbers

generator(2, 20)  # Outputs a list of odd numbers between 2 and 20

