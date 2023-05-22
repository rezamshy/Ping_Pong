import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3], 4]
new_list = copy.copy(old_list)

old_list[3]=0

print("Old list:", old_list)
print("New list:", new_list)

list1 = [1, 2, [3, 4]]
list2 = copy.copy(list1)

list2[0] = 5
list2[2][0] = 6

print(list1)  # Output: [1, 2, [6, 4]]
print(list2)  # Output: [5, 2, [6