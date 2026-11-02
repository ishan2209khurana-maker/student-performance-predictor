
print("===== Electricity Billing Management System =====")

customer_name = input("Enter Customer Name: ")
customer_id = int(input("Enter Customer ID: "))
units = float(input("Enter Electricity Units Consumed: "))

# Calculate bill according to slab rates

if units <= 100:
    bill = units * 3

elif units <= 200:
    bill = (100 * 3) + (units - 100) * 5

elif units <= 300:
    bill = (100 * 3) + (100 * 5) + (units - 200) * 7

else:
    bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10

# Additional Charges
meter_charge = 50
tax = bill * 0.05

total_bill = bill + meter_charge + tax

# Display Customer Summary

print("\n===== Customer Billing Summary =====")
print("Customer Name:", customer_name)
print("Customer ID:", customer_id)
print("Units Consumed:", units)
print("Electricity Charges: Rs.", bill)
print("Meter Charges: Rs.", meter_charge)
print("Tax (5%): Rs.", tax)
print("------------------------------------")
print("Total Bill: Rs.", total_bill)
print("====================================")
