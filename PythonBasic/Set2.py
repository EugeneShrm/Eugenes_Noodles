# Creating a list with some duplicate colors
rainbow_list = ["blue", "green", "yellow", "blue", "yellow", "red"]

# Converting the list to a set to remove duplicates
rainbow_set = set(rainbow_list)
print(rainbow_set)  # Output the set of unique colors
print(type(rainbow_set))  # Print the type of the variable (should be <class 'set'>)

# Creating a string with unique characters
letters_list = ('Create a set using the set() function '
                'from text to obtain unique characters '
                'contained in the text.')

# Converting the string to a set to get unique characters
letters_set = set(letters_list)
print(letters_set)  # Output the set of unique characters from the string
print(type(letters_set))  # Print the type of the variable (should be <class 'set'>)
