# Map, Filter and Lambda (anonym def for 1 time using) expressions

# map()
def sum_of_numbers(x):
    return x + x
number_list = [1, 2, 3, 4, 5, 6, 7]

result = map(sum_of_numbers, number_list)
print(result)

# or with cycle

for item in map(sum_of_numbers, number_list):
    print(item)

# another example

def is_a_in_str(string):
    if "a" in string.lower():
        print('"a" is found')
        return True
    else:
        print('"a" is not found')
        return False

string_list = ["abra-cadabra", "alah", "jesus", "bbb", "A"]

print(list(map(is_a_in_str, string_list)))
print()

# filter(def, iterable), def - only booling(True, False), iterable(list, tuple, etc)

def is_num_odd(num):
    return num % 2 ==1

number_list = [1, 2, 3, 4, 5, 6, 7]
num_list2 = [8, 9, 10, 11]
final_num_list = number_list + num_list2

odd_num_list = [num for num in final_num_list if is_num_odd(num)]
print(odd_num_list)

print(list(filter(is_num_odd, final_num_list)))

# or

for num in filter(is_num_odd, final_num_list):
    print(num)

# lambda epression

number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda num : num ** 3, number_list)))

# long version without lambda
def cube(num):
    return num ** 3

number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(cube, number_list)))

# lambda with filter

number_list = [1, 2, 3, 4, 5, 6, 7]

print(list(filter(lambda num: num % 2 == 1, number_list)))
print(list(filter(lambda num: num % 2 == 0, number_list)))