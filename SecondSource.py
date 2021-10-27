'''Maximum of two number in python'''

def maximum(a,b):
    if a>=b:
        print(a)
    else:
        print(b)

a = 12
b = 14
print(maximum(a,b))

''' Python program to find the maximum of two number using max function'''

a = 14
b = 16
print(max(a,b))

c = 70
d = 90
maximum = max(c,d)
print(maximum)


#Ternary Method

a = 2
b = 4
print(a if a>=b else b)
