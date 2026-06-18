# ==================================================================
# PROJECT 4: STATIC CURRENCY CONVERTER (USD TO INR)
# ======================================================
# Author: Bittu Kumar
# Description: Converts United States Dollars (USD) to Indian Rupees (INR)
#              using a hardcoded static exchange rate.
# ==================================================================

# --- STEP 1: CONFIGRATION & EXCHANGE RATE ---
# Define the fixed conversion rate. 1 USD = 94.46 INR (Current Market Rate)
exchange_rate = 94.6

# --- STEP 2: USER INTERFACE & INPUT COLLECTION ---
print("=========================================================")
print("          WELCOME TO THE CURRENCY CONVERTER              ")
print("=========================================================")

# Capture the dollar amount from the user and cast to float to precise math
usd_input = input("Enter the amount in USD ($): ")
usd_amount = float(usd_input)

# --- STEP 3: CONVERSION LOGIC ---
# Multiply the user's USD amount with our static exchange rate to get INR
inr_amount = usd_amount * exchange_rate

# --- STEP 4: FORMATED OUTPUT GENERATION ---
# Printing a clean financial receipt layout using tabs (\t)
print("\n==============================================")
print("               CONVERSION RECEIPT               ")
print("==============================================")
print("Amount in USD:\t\t$",usd_amount)
print("Exchange Rate:\t\t1 USD =",exchange_rate,"INR")
print("------------------------------------------------")
print("Total Amount in INR:\t₹",inr_amount)
print("==============================================")
print("\nThank you for using ourservice!")

