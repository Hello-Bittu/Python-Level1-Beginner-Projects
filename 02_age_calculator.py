# ==========================================
# PROJECT 2: AGE CALCULATOR
# ==========================================

print("--- Welcome to the Age Calculator ---\n")

# Step 1: Define the current year as a fixed variable
current_year = 2026

# Step 2: Take the birth year as an input from the user
birth_year = int(input("Enter your birth year (e.g., 2000): "))

# Step 3: Use if-else to validate the input and calculate age
if birth_year <= current_year and birth_year > 0:
    # Calculate the age
    age = current_year - birth_year

    # Step 4: Display the results beautifully
    print("\n-----------------------------------------------")
    print(f"Current Year: {current_year}")
    print(f"Your Birth Year: {birth_year}")
    print("-------------------------------------------")
    print(f"You are {age} years old in {current_year}!")
    print("-------------------------------------------")

else:
    # If the user enters an invalid year
    print("\nError: Invalid Birth Year! It cannot be in the future or less than 1.")
    