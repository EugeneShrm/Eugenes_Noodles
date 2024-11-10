nested_list = [[1, 2, 3], [4,5], [6,7,8,9], ["a",True, 10 ]]
# print(nested_list)
# print(nested_list[-1][-3])

for inner_list in nested_list:
    print(inner_list)

for inner_list in nested_list:
    for number in inner_list:
            print(number) 