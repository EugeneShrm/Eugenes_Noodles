#1
from random import randint  # randint function to generate random integers

# Initialize an empty list to store random numbers
ran_numbers = []

# Start a loop that runs until ran_numbers has 11 elements
while len(ran_numbers) < 11:
    var_random = randint(1, 10)  # Generate a random number between 1 and 10
    ran_numbers.append(var_random)  # Add the random number to ran_numbers list
    if var_random == 7:  # Check if the random number is 7
        print("It is number 7")  
        break  # if 7 is generated
print(ran_numbers) 

#2
from random import randint 

# Initialize a variable to store the random number and an empty list to store numbers
number = 0
my_list = []

# Start a loop that continues until the random number generated is 7
while number != 7:
    number = randint(1, 10)  # Generate a random number between 1 and 10
    my_list.append(number)  # Add the generated number to my_list

# Print the list of random numbers generated up to and including the number 7
print(my_list)
