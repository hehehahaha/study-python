def gcd(a, b):
    while a != 0:
        a, b = b % a, a
 
    return b
print(gcd(54,345))

'''
假如需要求 1997 和 615 两个正整数的最大公约数,用欧几里德算法，是这样进行的：
1997 / 615 = 3 (余 152)
615 / 152 = 4(余7)
152 / 7 = 21(余5)
7 / 5 = 1 (余2)
5 / 2 = 2 (余1)
2 / 1 = 2 (余0)
'''