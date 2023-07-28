print("Welcome to Meow Cat's Calculator. \nEnter your numbers to add them up.")
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

print("Welcome to Meow Cat's Calculator 2.0 \nEnter a number to cube it.")
def cube(number):
    return number*number*number
num3 = input("Enter a number: ")
print(cube(float(num3)))