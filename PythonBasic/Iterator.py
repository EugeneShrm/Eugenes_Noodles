#1
cars = ['bmw', 'audi', "honda"]
Iter = iter(cars) #iterator is doing sequence
print(next(Iter))
print(next(Iter))
print(next(Iter))
print()

#2
cars = ['bmw', 'audi', 'honda']
Iter = iter(cars)  # iterator is doing sequence
# Loop to iterate through the iterator three times
for _ in range(3):
    print(next(Iter))

#3
cars = ['bmw', 'audi', 'honda']
Iter = iter(cars)  # iterator is doing sequence
# Loop to iterate through the iterator nine times
    for _ in range(9):
    try:
        print(next(Iter))
    except StopIteration:
        Iter = iter(cars)  # Reset the iterator if it reaches the end of the list
        print(next(Iter))


#To allow the user to specify the number of cycles to repeat the running of all elements in the cars variable, you can prompt the user for input and use that value as the number of iterations. Here's the updated code:

#4
cars = ['bmw', 'audi', 'honda']
Iter = iter(cars)  # iterator is doing sequence

# Prompt the user to enter the number of cycles
num_cycles = 1 #or int(input("Enter the number of cycles: "))

# Loop to repeat the running of all elements in the cars variable
for _ in range(num_cycles):
    # Iterate through the cars list
    while True:
        try:
            car = next(Iter)
            print(car)
        except StopIteration:
            Iter = iter(cars)  # Reset the iterator if it reaches the end of the list
            break  #Exit the inner loop when all elements have been printed in current cycle
