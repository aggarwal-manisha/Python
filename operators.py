import math

a = input()
b = input()


class operators():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        result = self.x + self.y
        return result

    def subtraction(self):
        result = self.x - self.y
        return result

    def multiplication(self):
        result = self.x * self.y
        return result

    def division(self):
        #here result will be float
        result = self.x / self.y
        return result

    def floor_division(self):
        #also called ad integer division and resturn int value
        result = self.x // self.y
        return result

    def remainder(self):
        result = self.x % self.y
        return result

    def exponent(self):
        result = self.x ** self.y
        return result


print(math.floor(2.9)) #result --> 2

print(math.ceil(2.1))  #result -->3

print(math.pow(3,2))
#Relational operators

print(a > b) #greater then

print(a < b) #less then

print(a == b) # equal to

print(a >= b) # greater than equal to

print(a <= b) #less than equal to

print(a != b) # not equal to


#logical operators

print(a>8 and b<8) #true when both the conditions r true

print(a>8 or b<8) #true when any of  the conditions is true

a = True

print(not a) #revere the result


#binary operators

#:--> decimal to binary

print(bin(25))

#:--> decimal to octal

print(oct(25))

#:--> decimal to hexadecimal

print(hex(25))