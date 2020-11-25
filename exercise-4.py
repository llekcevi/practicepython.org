"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number."""

x = int(input("Enter a number: "))

a = [elem for elem in range (1, x+1) if x % elem == 0 ]

print (a)
