import operator

def calculator():
    try:
        num1 = int(input("Enter number: "))
        #ask the user to pick an operator
        opt = input("Pick operator(+,-,*,/): ")
        num2 = int(input("Enter another number: "))
        if opt not in ['+', '-', '*', '/'] or len(opt) > 1:
            print("Please enter a valid operator.")
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("You can not divide by zero. Try again.")
    else:
        if opt == '+':
            return f'{num1} {opt} {num2} is: {operator.add(num1, num2)}'
        elif opt == '-':
            return f'{num1} {opt} {num2} is: {operator.sub(num1, num2)}'
        elif opt == '*':
            return f'{num1} {opt} {num2} is: {operator.mul(num1, num2)}'
        elif opt == '/':
            return f'{num1} {opt} {num2} is: {operator.truediv(num1, num2)}'
    return "Try again."

print(calculator())
