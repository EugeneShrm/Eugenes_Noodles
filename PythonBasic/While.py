# Initialize variable x with a value of 5
x = 5

# While loop to print numbers from x down to 1
while x >= 1:
    print(x)  # Print the current value of x
    x = x - 1  # Decrease x by 1

# Initialize variable a with a value of 0
a = 0

# While loop to print a message while a is less than 10
while a < 10:
    print("X is less than 10")  # Print the message
    a += 2  # Increment a by 2

# Check the value of a after exiting the loop
if a == 10:
    print("a equals 10")  # Print if a is equal to 10
    a += 2  # Increment a by 2
elif a > 10:
    print("a is more than 10")  # Print if a is greater than 10

import random  # Import the random module

# Generate a random integer between 1 and 10
random_var = random.randint(1, 10)

# While loop to print the random variable if it is between 1 and 10
while random_var > 0 and random_var < 11:
    print(random_var)  # Print the random variable
    if random_var == 7:
        break  # Exit the loop if the random variable is 7

# Initialize an empty list to store random numbers
random_numbers = []

# Generate 10 random numbers between 1 and 10
for _ in range(10):
    random_var = random.randint(1, 10)  # Generate a random number
    random_numbers.append(random_var)  # Add the random number to the list
    if random_var == 7:
        break  # Exit the loop if the random number is 7

# Print the list of random numbers generated
print(random_numbers)

