import copy

list1 = [[1, 2, 3], [4, 5, 6], [7, 8]]

list2 = copy.deepcopy(list1)
list1 = [[0, 1, 2, 3], [4, 5, 6], [7, 8]]
print(list1)
print(list2)

print("Hello World")


def my_function():
    print("Hello from a function")


my_function()
