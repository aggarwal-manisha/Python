'''
Print all the values from 1 to 100 which are not divisible by 3 or 5.

output should be in following format

# # # #
# # # #
# # # #
'''

def pattern():

    x = 1
    y = 1
    while x <= 100:
        if x % 3 != 0 or x % 5 != 0:
            pass
        else:
            if y % 5 == 0:
                print('\n')
            else:
                print(x, ' ', end='')
            y += 1

        x += 1

pattern()


