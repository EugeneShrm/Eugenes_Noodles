#Basic while cycle
i = 1
while i<=10:
    print(i)
    i += 1

#While + if cycle with skip number condition
c = 0
while c<12:
    c += 2
    if c == 4: #to skip 4
        continue
    print(c)
    if c == 12:
        print("done")

#Iterate over a list of integers and concatenate a string to each integer
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in number_list: # Iterate over each element in the list
    print(str(x)+ " " + "Tokyo")

#Iterate over a list of integers and define if it is even or odd 
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in number_list:  # Iterate over each element in the list
    if x % 2 == 0: # Check if the integer is even
        print(x)
    else:
        print("Odd")

#sum of the integers in the list
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_sum = 0 # Initialize a variable to hold the cumulative sum
for number in number_list: # Iterate over each number in the list
    list_sum = list_sum + number # Add the current number to the cumulative sum
    print(list_sum)

#Two separate for loops that iterate through the string
letter_var = "Tokyo"
for letter in letter_var:
    if letter == "o":
        continue # print everything except "o"
    print(letter)
for letter in letter_var:
    if letter == "o": # print only "o"
        print(letter)

