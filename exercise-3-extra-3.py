""" Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5. """

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_num = []
num = int(input("Pick a number."))

for element in a:
    if element <= num:
        less_than_num.append(element)

print(f" The numbers that are less than {num} are {less_than_num} .")
        
