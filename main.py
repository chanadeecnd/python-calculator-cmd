from replit import clear
from logo import logo

print(logo)

result = 0


def calculate(input1, input2, operator):

    def sums(input1, input2):
        return input1 + input2

    def subtract(input1, input2):
        return input1 - input2

    def multiply(input1, input2):
        return input1 * input2

    def divide(input1, input2):
        return input1 / input2
    
    if operator == "+":
        result = sums(input1, input2)
    elif operator == "-":
        result = subtract(input1, input2)
    elif operator == "*":
        result = multiply(input1, input2)
    elif operator == "/":
        result = divide(input1, input2)

    return result


def main():
    while True:
        input1 = float(input("What's the first number?: "))
        print("+\n-\n*\n/\n")
        operator = str(input("Pick an operation: "))
        input2 = float(input("What's the next number?: "))

        result = calculate(input1, input2, operator)
        print(f"{input1} {operator} {input2} = {result}")

        result_log = result
        while True:
            continue_cal = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "))
            if continue_cal == "y":
                next_operator = str(input("Pick an operation: "))
                next_number = float(input("What's the next number?: "))
                result = calculate(result_log, next_number, next_operator)
                print(f"{result_log} {next_operator} {next_number} = {result}")
                result_log = result
            else:
                result_log = 0
                result = 0
                clear()
                break

if __name__ == "__main__":
    main()
