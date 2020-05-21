
a = 10
b = 9
print(id(a))

def variable():
     a = 15 #local var
     print(id(a))
     globals()['a']=19
                                 # x = globals()['a'] #global var
     y = globals()['b']
     print(id(globals()['a']))

variable()
print(id(a))
print(a)




#count the odd and even numbers in a list

def lis(lis):
    even = 0
    odd = 0
    for obj in lis:
        if obj % 2 ==0:
            even+=1
        else:
            odd +=1

    return even, odd

data = [1,2,3,5]
even, odd = lis(data)

print("Even: {}, Odd: {}".format(even, odd))