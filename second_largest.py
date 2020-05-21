
li = map(int, input().split(','))
lis = list(li)

lis.sort()
lis.reverse()

for i in lis:
    if i != lis[0]:
        print(i)
        break