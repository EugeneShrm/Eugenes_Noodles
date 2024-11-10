#Excercise 1
total_sum = 0
for x in range(10, 31):
    if x % 2 == 0:
        total_sum += x
print(total_sum)

#Excercise 2
i = 0
for n in range(10, 31):
    if n % 2 == 0:
        i += n
print(i)

# Print Hello n times according to user input
user_input = int(input("Enter some number: "))
for _ in range(user_input):
    print("Hello")

