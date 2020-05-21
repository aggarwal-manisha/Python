

def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        lis = [a]
    elif n == 2:
        lis = [a, b]
    else:
        lis = [0, 1]
        for i in range(n):
            c = a+b
            a = b
            b = c
            lis.append(c)

    print(lis)
    return lis

fibonacci(10)