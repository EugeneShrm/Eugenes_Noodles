# With List Comprehension
def get_odd_number_list(a, b):
    number_list = list(range(a, b + 1))
    odd_number_list = [number for number in number_list if number % 2 == 1]
    return odd_number_list


# Without List Comprehension
def get_odd_number_list(a, b):
    number_list = list(range(a, b+1))
    odd_number_list = []
    for number in number_list:
        if number % 2 == 1:
            odd_number_list.append(number)
    return odd_number_list
print(get_odd_number_list(2, 20))