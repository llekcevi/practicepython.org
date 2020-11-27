import random

randomlist1 = []                    #two random lists, and one for storing overlapping numbers
randomlist2 = []
random_overlap = []

for i in range(0,5):                #creating two random list with 5 numbers in range 1-30
    n = random.randint(1,30)
    randomlist1.append(n)

    m = random.randint(1,30)
    randomlist2.append(m)

print(randomlist1, randomlist2)     #it seems useful to see the randomly generated lists

for x in randomlist1:               #for every element of the first list it looks for the same element
    if x in randomlist2:            #in the second list"
        random_overlap.append(x)    #adds the overlaping element in the third list
print(random_overlap)

        
