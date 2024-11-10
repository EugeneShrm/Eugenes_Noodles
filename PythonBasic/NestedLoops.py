# VARIANT 1
smile = '\U0001f600'
counter = 1  # Counter to limit the number of iterations
while counter <= 10:  # Loop will run 10 times
    print(smile * counter)  # Print the smiley face multiplied by the counter
    counter += 1  # Increment the counter


# VARIANT 2
for number in range(10):
    counter = 0
    smile = '\U0001f600'
    while counter <= number:
        smile += '\U0001f600'
        counter += 1
    print(smile)

# VARIANT 3
for number in range(10):
    smile = '\U0001f600'
    for _ in range(number + 1):  #
        smile += '\U0001f600'
    print(smile)

# VARIANT 4
for number in range(1, 11):
    print('\U0001f600' * number)
