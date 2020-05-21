'''
*
* *
* * *
* * * *
* * * * *
'''

def pattern1(n):
    for i in range(1, n):
        for j in range(1, n+1):
            if i >= j:
                print("*", end="")
        print()

pattern1(6)


'''
        *
      * *
    * * *
  * * * *
* * * * *

'''

'''
      *
    * * *
  * * * * *
* * * * * * *
'''
