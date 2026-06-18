# ================================================
# PROJECT 3: CELSIUS TO FAHRENHEIT CONVERTER
# ================================================

# Step 1: Display a clean, formatted title
print("--- WELCOME TO THE TEMPERATURE CONVERTER ---")
print("Convert your Celsius values to Fahrenheit instantly.\n")

# Step 2 & 3: Take user input and immediately type cast it to float
celsius_input = input("Enter temperature in Celsius (e.g., 37.5): ")
celsius = float(celsius_input)

# Step 4: Apply the mathematical formula
# Formula: (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Step 5: Display the final result using escape sequence for formatting
print("\n--- CONVERSION RESULT ---")
print("\tInput Temperature:\t", celsius, "°C")
print("\tConverted Output:\t", fahrenheit, "°F")
print("-----------------------------------------------")