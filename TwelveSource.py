''' Sum of first n natural number '''
def squareNumber(n):
    sm = 0
    for i in range(1,n+1):
        sm = sm+(i*i)
    return sm

n = 4
print(squareNumber(n))
                
