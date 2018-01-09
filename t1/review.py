# 1. let's say we have a matrix which is a list of lists

row = [0, 0]
matrix = [row, row]
print(matrix)  # what's the output?

matrix[0][0] = 1
print(matrix)  # what's the output?

row[1] = 3
print(matrix)  # what's the output?


# 2. mutating lists

def append_to_list(array, item):
    array += [item]


def append_to_list2(array, item):
    array.append(item)


my_list = [1, 2, "three"]
append_to_list(my_list, "Hello")
append_to_list2(my_list, "Yufei")
print(my_list)  # what's the output?

# 3. More stuff

list1 = [11, 99, [4, 5]]
list2 = list1  # not a true copy! just copies the reference
print(list1 is list2)
list2[2][0] = "BOO!"
print(list1)  # what's the output?

list3 = list1[:]
print(list1 is list3)
list3[2][0] = "WOO!"
print(list1)  # what's the output?

import copy
list4 = copy.deepcopy(list1)
print(list1 is list4)
list4[2][0] = "FOO!"
print(list1)  # what's the output?

