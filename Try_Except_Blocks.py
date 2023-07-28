try:
    number = int(input("Enter an integer: "))
    print(number)
except:
    print("Invalid Input")

try:
    #value = 10/0
    number = int(input("Enter an integer: "))
    print(number)
except ZeroDivisionError:
    print("There is division by zero somewhere.")
except ValueError:
    print("Invalid Input")

try:
    number = int(input("Enter an integer: "))
    print(number)
    value = 10/0
except ZeroDivisionError:
    print("There is division by zero somewhere.")
except ValueError:
    print("Invalid Input")