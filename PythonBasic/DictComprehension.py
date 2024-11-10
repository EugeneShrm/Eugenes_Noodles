# Define a list of numbers with both positive and negative integers
number_list = [6, 43, -2, 11, -55, -12, 3, 444]

# Create a dictionary using a dictionary comprehension
# The comprehension iterates through each number in number_list
# and sets each number as both the key and value in number_dict
number_dict = {number: number for number in number_list}

# Print the resulting dictionary where each number from the list
# is both a key and its corresponding value
print(number_dict)