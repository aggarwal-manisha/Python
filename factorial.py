#recursion is calling a function by itself

def factorial(num):
    if num == 0:
        return 1
    num *= factorial(num-1)
    return num

factorial(5)