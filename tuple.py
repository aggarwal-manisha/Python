"""
--> tuples are immutable(they cannot be changed)
--> iteration is faster in tuple than list
"""

tup = (10, 20, 30, 10)

print(tup[1]) #-->result 20

tup[1] = 33 # throws error as tuples r immutable

#counts tell the number of occurance of that paricular element
tup.count(10) #result --> 2

# returns the index of that particular element
tup.index(20) #result --> 1

