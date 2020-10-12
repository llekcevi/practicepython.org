print("Input two numbers.")
check = int(input("Please input a number to check: "))
num = int(input("Please input a number to divide by: "))

if check % num == 0:
    print("The numbers you have entered divide evenly.")
else:
    print("The numbers you have entered do not divide evenly.")
    