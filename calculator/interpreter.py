from math_utils.math_utils import add
from math_utils.math_utils import subtract
from math_utils.math_utils import multiply
from math_utils.math_utils import divide
def interpret(input_str):
    parts = input_str.strip().split()

    if len(parts) != 3:
        return "Invalid input format"

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        return "Invalid numbers."

    if op == "+":
        assert add(num1,num2) == num1 + num2
        return add(num1, num2)
    elif op == "-":
        assert subtract(num1,num2) == num1 - num2
        return subtract(num1, num2)
    elif op == "*":
        assert multiply(num1,num2) == num1 * num2
        return multiply(num1, num2)
    elif op == "/":
        assert divide(num1,num2) == num1 / num2
        return divide(num1, num2)
    else:
        return f"Unknown operator '{op}'. Use one of: +, -, *, /"
    
