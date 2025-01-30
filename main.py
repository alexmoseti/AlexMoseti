# Disconunt Program
amount = int(input("Enter amount: "))
if (amount >= 5000):
    discount = amount * 0.10
    print("Discount is:", discount)
    final_amount = amount - discount
    print("Amount to be paid is:", final_amount)

elif (4999 < amount > 1000):
    discount = amount * 0.05
    print("Discount is:", discount)
    final_amount = amount - discount
    print("Amount to be paid is:", final_amount)

else:
    print("NO discount to be applied")
    print("Amount to be paid is:  ", amount)