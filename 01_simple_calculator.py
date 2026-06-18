# ==========================================
# PROJECT 1: STANDARD SIMPLE CALCULATOR
# ==========================================

print("--- Welcome to the Simple Calculator ---\n")

# Step 1: Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform arithmetic operations and print results
print("\n---------------------------------------------------")
print("\t\t CALCULATOR RESULTS")
print("---------------------------------------------------")
print(f"Addition ({num1} + {num2})          = {num1 + num2}")
print(f"Substraction ({num1} - {num2})      = {num1 - num2}")
print(f"Multiplication ({num1} * {num2})    = {num1 * num2}")

# Step 3: Handle the division-by-zero edge using if-else
if num2 != 0:
    print(f"Division ({num1} / {num2})          = {num1 / num2}")
else:
    print("Division (Error)               = Cannot divide by zero!")
print("--------------------------------------")