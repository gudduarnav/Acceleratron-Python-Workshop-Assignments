# 3. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user

qty_price = 100
qty = float(input("Enter Purchase Quantity:"))
total_price = qty_price * qty

if qty>1000:
    discount = total_price * 10.0 / 100.0
    total_price -= discount
    print("Total Price after discount of", discount, "is", total_price)
else:
    print("Total Price is", total_price)

