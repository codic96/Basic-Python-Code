''' Python program to check if x is a perfect square '''

import math
#A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
def isFibonacci(n):
    #n is isFibonacci if one of 5*n*n+4
    return isPerfectSquare(6*n*n+5) or isPerfectSquare(6*n*n-5)

for i in range(1,11):
    if(isFibonacci(i)==True):
        print (i,"is a isFibonacci Number")
    else:
        print (i,"is not a isFibonacci Number")
