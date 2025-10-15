import math

print("=== Advanced Calculator ===")
print("Available operations: +, -, *, /, pow, sqrt, sin, cos, tan")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operation: ")

match op:
    # ➕ Arithmetic Operations
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b == 0:
            print("Error: Division by zero")
        else:
            print("Result:", a / b)

    # 🔹 Power Function
    case "pow":
        choose = input("Select number to square (a/b): ")
        match choose:
            case "a":
                print("Result:", math.pow(a, 2))
            case "b":
                print("Result:", math.pow(b, 2))
            case _:
                print("Invalid choice! Please enter 'a' or 'b'.")

    # 🔹 Square Root
    case "sqrt":
        choose = input("Find square root of (a/b): ")
        match choose:
            case "a":
                if a < 0:
                    print("Error: Square root of negative number")
                else:
                    print("Result:", math.sqrt(a))
            case "b":
                if b < 0:
                    print("Error: Square root of negative number")
                else:
                    print("Result:", math.sqrt(b))
            case _:
                print("Invalid choice! Please enter 'a' or 'b'.")

    # 🔹 Trigonometric Functions
    case "sin":
        choose = input("Apply sin on (a/b): ")
        match choose:
            case "a":
                print(f"sin({a}°) =", round(math.sin(math.radians(a)), 4))
            case "b":
                print(f"sin({b}°) =", round(math.sin(math.radians(b)), 4))
            case _:
                print("Invalid choice! Please enter 'a' or 'b'.")

    case "cos":
        choose = input("Apply cos on (a/b): ")
        match choose:
            case "a":
                print(f"cos({a}°) =", round(math.cos(math.radians(a)), 4))
            case "b":
                print(f"cos({b}°) =", round(math.cos(math.radians(b)), 4))
            case _:
                print("Invalid choice! Please enter 'a' or 'b'.")

    case "tan":
        choose = input("Apply tan on (a/b): ")
        match choose:
            case "a":
                print(f"tan({a}°) =", round(math.tan(math.radians(a)), 4))
            case "b":
                print(f"tan({b}°) =", round(math.tan(math.radians(b)), 4))
            case _:
                print("Invalid choice! Please enter 'a' or 'b'.")
    case _:
        print("Invalid operation!")
