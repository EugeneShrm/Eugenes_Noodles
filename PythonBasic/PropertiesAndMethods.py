# Performing division and storing the result
floatR = 1000 / 7
# Formatting the result to 3 decimal places
print('{0:3.3f}'.format(floatR))
# Formatting the result to 4 significant figures
print('the result of division is {0:5.4}'.format(floatR))

# Multi-line formatted string with various floating-point values
print('''
{0:2.2f}' '{1:2.2f}' '{3:2.2f}
{4:2.2f}' '{6:2.2f}' '{5:2.2f}
{7:2.2f}  {2:2.2f}  {8:2.2f}
'''.format(123.55555, 4444.666, 6666.77, 8888.888, 123.55555, 4444.666, 6666.77, 8888.888, 6666.9999))

# Assigning values to variables
name = "Jack"
age = 23
# Using f-string for formatted output
print(f"His name is {name}. he is {age} years old.")

# Creating a new list with mixed data types
new_list = [1, 3, 'Word', 3.55]
# Slicing the new list to create a second list with the first three elements
second_list = new_list[:3]
# Printing the sliced list
print(second_list)
