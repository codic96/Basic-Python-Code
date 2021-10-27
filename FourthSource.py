''' Python Program for Simple Interest '''

'''Simple Interest = (P*R*T)/100 '''

def simple_interest(p,r,t):
    print('The principle is',p)
    print('The time period is',r)
    print('the rate of Interest is',t)
    simple_interest = (p*r*t)/100
    print('The simple Interest is ',simple_interest)

print(simple_interest(12,8,3))


'''Python Program for Compound Interest'''
import math

def Compound_interest(principle,rate,time):
    amount = principle*(pow((1+rate/100),time))
    Compound = amount-principle
    print('The Compound intest are',Compound)

print(Compound_interest(100000,10.25,5))
