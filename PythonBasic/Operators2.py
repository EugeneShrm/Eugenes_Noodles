# Print each character in the string "Hello"
for x in "Hello":
    print(x)

# Nested loops to print the values of i, j, and p
for i in range(3):  # Outer loop runs 3 times
    for j in range(2):  # Middle loop runs 2 times
        for p in range(1):  # Inner loop runs 1 time
            print(i, j, p)

# Create a list of numbers from 0 to 1000, incrementing by 25
x = list(range(0, 1000, 25))
print(x)

# List of fruits
fruits = ["apple", "banana", "cherry"]

# Print each fruit with its index
for index, fruit in enumerate(fruits):  # Adding index
    print(index, fruit)

# Print the Unicode code point of each letter in "Hello"
for letter in "Hello":
    print(ord(letter))

# Find the minimum character in the string "Hello"
letter = "Hello"
print(min(letter))  # Returns the character with the lowest Unicode value

# Convert greeting into a list of its letters
greeting = "Hello"
letter_list = []
for letter in greeting:
    letter_list.append(letter)  # Append each letter to letter_list
print(letter_list)

# Using list comprehension to create a list of letters from greeting
greeting = "Hello"
letter_list = [letter for letter in greeting]
print(letter_list)

# Create a list of digits as strings from "0123456789"
number_list = [number for number in "0123456789"]
print(number_list)

# Square positive numbers from number_list2 and create a new list
number_list2 = [5, 66, -77, -3, 6, 0, -5, 111]
new_list = [num ** 2 for num in number_list2 if num > 0]  # Only includes positive numbers
print(new_list)

# Create a list of "+" for positive numbers and "-" for non-positive numbers
new_list2 = ["+" if num > 0 else "-" for num in number_list2]
print(new_list2)

# Extract the second letter from each greeting
greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = []
for letter in greetings:
    letter_list.append(letter[1])  # Append the second character of each greeting
print(letter_list)

# Using list comprehension to get the second letter from each greeting
greetings = ['hello', 'hi', 'hey', 'hola']
new_list = [num[1] for num in greetings]  # Get the second character of each string
print(new_list)

# Create a list of odd numbers from the digits list
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = [num for num in digits if num % 2 != 0]  # Only includes odd numbers
print(odd_numbers)

# Using a for loop to collect odd numbers from digits
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = []
for num in digits:
    if num % 2 != 0: 
        odd_numbers.append(num)  # Append odd numbers to the list

print(odd_numbers)



