# 1
x = 5
while x >= 1: # While loop to print numbers from x down to 1
    print(x)  # Print the current value of x
    x = x - 1  # Decrease x by 1

#2
a = 0 #Initialize variable a with a value of 0
while a < 10: # While loop to print a message while a is less than 10
    print("X is less than 10")  # Print the message
    a += 2  # Increment a by 2

# Check the value of a after exiting the loop
a = 2
if a == 10:
    print("a equals 10")  # Print if a is equal to 10
    a += 2  # Increment a by 2
elif a > 10:
    print("a is more than 10")  # Print if a is greater than 10
else:
    print("a is less than 10")  # Print if a is greater than 10


import random  # Import the random module

# Number Loop 
random_var = random.randint(1, 10) #Initialize an empty list to store random numbers
while random_var > 0 and random_var < 11: # While loop to print the random variable if it is between 1 and 10
    print(random_var)  # Print the random variable
    if random_var == 7:
        print("Found a 7, breaking out of the loop.")
        break  # Exit the loop if the random variable is 7
    random_var = random.randint(1, 10)

# Generate 10 random numbers between 1 and 10 
random_numbers = [] #Initialize an empty list to store random numbers
for _ in range(10):
    random_var = random.randint(1, 10)  # Generate 10 random numbers between 1 and 10
    random_numbers.append(random_var)  # Add the random number to the list
    if random_var == 7:
        break  # Exit the loop if the random number is 7

# Print the list of random numbers generated
print(random_numbers)



