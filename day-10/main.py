from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_continue = True
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while should_continue:
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculate = operations[operator]
        answer = calculate(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        ask_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
        if ask_continue == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

print(logo)

calculator()