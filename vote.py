citizen = input("Enter your citizenship: ")
age = int(input("Enter your age: "))
if (citizen == "Kenyan" and age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")