def prime(n):
    for i in range(3, n):
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print(i)
 