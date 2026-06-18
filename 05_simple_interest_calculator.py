# =========================================
# PROJECT 5: SIMPLE INTEREST CALCULATOR
# =========================================

# Step 1: Taking inputs from the user
print("--- Welcome to the Simple Interest Calculator ---\n")

principal = float(input("Step 1: Enter Principal amount: "))
rate = float(input("Step 2: Enter the Rate of Interest (in %): "))
time = float(input("Step 3: Enter time (in years): "))

# Step 2: Calculating Simple Interest
simple_interest = (principal * rate * time) / 100

# Step 3: Calculating Total Maturity Amount
total_amount = principal + simple_interest

# Step 4: Printing the Final Report Card/Receipt
print("\n------------------------------------------------------------")
print("\t\t LOAN INVESTMENT SUMMARY")
print("------------------------------------------------------------")
print(f"Principal Amount:\t {principal}")
print(f"Interest Rate:\t\t {rate}%")
print(f"Time Period:\t\t {time} years")
print("----------------------------------------------")
print(f"Simple Interest Earned: {simple_interest}")
print(f"Total Payable Amount: {total_amount}")
print("----------------------------------------------")