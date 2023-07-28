def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

number_1 = float(input("Enter a number:"))
number_2 = float(input("Enter another number:"))
number_3 = float(input("Enter one last number:"))
print(max_num(number_1, number_2, number_3))

# comparators include == (equals), >= (greater than or equals), <= (less than or equals), > (greater than) and < (less than). 