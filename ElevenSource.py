''' Python program for n/th multiple of a number '''

def findposition(k,n):
    f1 = 0
    f2 = 1
    i = 2
    while i!=0:
        f3 = f1+f2
        f1 = f2
        f2 = f3
        if f2%k==0:
            return n*i
        i+=1
    return

n = 5;
k = 4;
print('Position of multiple of K number',findposition(n,k));


''' Program to print ASCII value of a character '''

c = 'g'
print("The ASCII value of ''"+c+"'is",ord(c))
