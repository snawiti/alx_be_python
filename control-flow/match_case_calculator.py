num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        print("The result is ", (num1 + num2), ".")
    case "-":
        print("The result is ", (num1 - num2), ".")
    case "*":
        print("The result is ", (num1 * num2), ".")
    case "/":
        print("The result is ", (num1 / num2), ".") 
    case _:
        print("invalid input")
