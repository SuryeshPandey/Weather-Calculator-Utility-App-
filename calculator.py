# calculator.py

from logger import log_event
import re

def is_valid_expression(expr):
    # Only allow numbers, + - * / ( ) and dots
    return bool(re.match(r'^[\d\s\.\+\-\*\/\(\)]+$', expr))

def calculator_cli():
    print("\n📐 Calculator Mode")
    print("Type expressions like: 5 + 2 or 10 / 3")
    print("Type 'exit' to return to main menu\n")

    while True:
        expr = input("➤ Enter operation: ").strip()

        if expr.lower() == "exit":
            break

        if not is_valid_expression(expr):
            print("❌ Invalid input. Use only numbers and + - * /")
            log_event(f"Invalid expression attempted: {expr}")
            continue

        try:
            # Avoid evaluating if expression is empty or only an operator
            if expr in ["+", "-", "*", "/", ""]:
                raise SyntaxError("Incomplete expression")

            result = eval(expr)
            print(f"✅ Result: {result}")
            log_event(f"Calculation: {expr} = {result}")
        except ZeroDivisionError:
            print("❌ Error: Cannot divide by zero.")
            log_event(f"Calculation error (divide by zero): {expr}")
        except SyntaxError:
            print("❌ Error: Incomplete expression.")
            log_event(f"Calculation error (incomplete): {expr}")
        except Exception as e:
            print(f"❌ Error: {e}")
            log_event(f"Calculation error ({e}): {expr}")
