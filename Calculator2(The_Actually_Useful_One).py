print("Welcome to Meow Cat's Actually Useful Calculator. \nIt can solve any basic arithmetic equation.")
print("Valid operators are + for addition, - for subtraction, / for division and * multiplication. You can also write \"End\" in place of an operator to end the program.")
while True:
    num1 = float(input("Enter the first number in your equation: "))
    op = input("Enter the operator: ")
    num2 = float(input("Enter the second number: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "End":
        break
    else:
        print("Please enter a valid operator.")
print("The program is finished.")