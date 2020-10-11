print("Welcome! \n ""Input your name and age.")

#asks user for name and age
name = input("What's your name? ")
age = int(input("How old are you? "))

#calculates and displays when a person will turn 100 years old
hundred = 2020 + (100 - age)
hundred = str(hundred)
print("You will turn 100 in year: " + hundred)

#extras 1 and 2: exact number of copies of the previous message
number = int(input("How many times do you want to see the message? "))
for x in range(number):
    print("You will turn 100 in year: " + hundred)
