''' Python program to find sum of series '''

def sumofSeries(n):
    sum = 0
    for i in range(1,n+1):
        sum += i*i*i
    return sum

n = 5
print(sumofSeries(n))
        
