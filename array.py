'''
i --> integer
l --> long
f --> float
d --> double
b --> char
'''

from array import *

val = array('i', [])

n = int(input("Enter the length of the array"))

for i in range(n):
    val = int(input("Enter the next value"))
    val.append(val)

print(val)

val_to_search = int(input("Enter the value to search"))

print(val.index(val_to_search))

#print the array
for obj in val:
    print(obj, end='')
print('\r')

#to find the memory location and size of an array
print(val.buffer_info())

#insert value in the end of an array
val.append(4)
for obj in val:
    print(obj, end='')
print('\r')

# insert a value 78 at index 3
val.insert(2, 5)
for obj in val:
    print(obj, end='')
print('\r')

# pop removes the value at the mentioned index
val.pop(2)
for obj in val:
    print(obj, end='')
print('\r')

#remove ,removes the 1st occurance of that element
val.remove(3)
for obj in val:
    print(obj, end='')
print('\r')


#index function returns the index of the first occurance element
val.index(3)

#reverse function reverse the array
val.reverse()
print(val)


