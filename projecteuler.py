# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 11:42:26 2016

@author: magfrump
"""
import time
import numpy as np
import math

#Problem 580

total = 2327192
def is_not_divis(x,stuff):
    for item in stuff:
        if x%item== 0:
            return False
        if item > x:
            return True
    return True

try:
    print len(primes)
except:
    primes = [2,3,5,7,11,13,17,19,23]
nextnum = 29
while(primes[-1]< 10**8):
    if is_not_divis(nextnum,primes):
        primes.append(nextnum)
    nextnum+=2

def is_squarefree(x,primes):
    for p in primes:
        if x%(p**2)==0:
            return False
        if p**2 > x:
            return True
    return True

for k in range(25*10**5,24*10**14):
    if k%10**5==0:
        print k
    hil = 4*k+1
    if is_squarefree(hil):
        total+=1

print total
    


## Problem 35
#
#def is_not_divis(x,stuff):
#    for item in stuff:
#        if x%item== 0:
#            return False
#        if item > x:
#            return True
#    return True
#
#try:
#    print len(primes)
#except:
#    primes = [2,3,5,7,11,13,17,19,23]
#nextnum = 29
#while(primes[-1]<1000000):
#    if is_not_divis(nextnum,primes):
#        primes.append(nextnum)
#    nextnum+=2
#    
#def is_prime(x,primes):
#    if x<2:
#        return False
#    if x in primes:
#        return True
#    elif is_not_divis(x,primes):
#        return is_not_divis(x,range(primes[-1],int(np.sqrt(x))))
#    else:
#        return False
#
#circprimes = []
#
#def is_circ(p):
#    numdig = len(str(p))
#    rots = [p]
#    if numdig == 1:
#        return rots
#    for i in range(1,numdig):
#        rot = p//(10**i) + (10**(numdig-i))*(p%10**i)
#        if rot in primes:
#            rots.append(rot)
#        else:
#            return []
#    print rots
#    return rots
#    
#for p in primes:
#    circprimes+=is_circ(p)
#
#print len(set(circprimes))


##Problem 34
#
#total = 0
#
#for x in range(13,1999999):
#    digsum = 0
#    for dig in str(x):
#        digsum+=math.factorial(int(dig))
#        if digsum>x:
#            break
#    if digsum==x:
#        total+=x
#
#print total

## Problem 33
#
#for x in range(11,100):
#    for y in range(x+1,100):
#        if(x%10==y%10 and x%10!=0 and 1.0*x/y == 1.0*(x//10)/(y//10)):
#            print x,y
#        elif(x//10 == y%10 and 1.0*x/y == 1.0*(x%10)/(y//10)):
#            print x,y
#        elif(x%10 == y//10 and y%10!=0 and 1.0*x/y == 1.0*(x//10)/(y%10)):
#            print x,y
#        elif(x//10 == y//10 and y%10!=0 and 1.0*x/y == 1.0*(x%10)/(y%10)):
#            print x,y
#




# Problem 32


#def is_pandigital(x,y):
#    digits = range(1,10)
#    xdig = x
#    while xdig>0:
#        if xdig%10 not in digits:
#            #print x,xdig%10
#            return False
#        else:
#            digits.pop(digits.index(xdig%10))
#            xdig = (xdig-xdig%10)/10
#    xdig = y
#    while xdig>0:
#        if xdig%10 not in digits:
#            #print x,y,xdig%10
#            return False
#        else:
#            digits.pop(digits.index(xdig%10))
#            xdig = (xdig-xdig%10)/10
#    xdig = x*y
#    while xdig>0:
#        if xdig%10 not in digits:
#            #print x,y,x*y,xdig%10
#            return False
#        else:
#            digits.pop(digits.index(xdig%10))
#            xdig = (xdig-xdig%10)/10
#    if len(digits)==0:
#        return True
#    else:
#        return False
#        
#pandig = []
#for x in range(98):
#    for y in range(x,9876):
#        if is_pandigital(x,y):
#            pandig.append(x*y)
#
#print sum(set(pandig))

## Problem 31
#
#values = [200,100,50,20,10,5,2]
#
#total = 1 #manually count 1x200
#
#for x in range(101):
#    for xy in range(41):
#        for y in range(21):
#            for z in range(11):
#                for a in range(5):
#                    for b in range(3):
#                        if 100*b+50*a+20*z+10*y+5*xy + 2*x <=200:
#                            total+=1
#                        
#print total


## Problem 30
#def sum_fifth(x):
#    total = 0
#    while x>0:
#        total += (x%10)**5
#        x = x//10
#    return total
#
#total = 0
#for x in range(295488):
#    if x==sum_fifth(x):
#        total+=x
#        
#print total
#    


## Problem 29
#
#powers = []
#for a in range(2,101):
#    for b in range(2,101):
#        powers.append(a**b)
#        
#print len(set(powers))


##Problem 28
#
#total = 1
#currentnum = 1
#for x in range(1,501):
#    #500 layers give 1001 on a side
#    for y in range(0,4):
#        #four corners for each layer
#        currentnum += 2*x
#        total += currentnum
#
#print total

## Problem 27
#
#def is_not_divis(x,stuff):
#    for item in stuff:
#        if x%item== 0:
#            return False
#        if item > x:
#            return True
#    return True
#
#primes = [2,3,5,7,11,13,17,19,23]
#nextnum = 29
#while(len(primes)<10001):
#    if is_not_divis(nextnum,primes):
#        primes.append(nextnum)
#    nextnum+=2
#    
#def is_prime(x,primes):
#    if x<2:
#        return False
#    if x in primes:
#        return True
#    elif is_not_divis(x,primes):
#        return is_not_divis(x,range(primes[-1],int(np.sqrt(x))))
#    else:
#        return False
#
#maxa = 1
#maxb = 41
#maxn = 40
#for a in range(-999,1000):
#    for b in range(-1000,1001):
#        n=0
#        conprime = 0
#        while(is_prime(n*n+a*n + b,primes)):
#            conprime +=1
#            n+=1
#        if conprime > maxn:
#            print a,b,conprime
#            maxn = conprime
#            maxa = a
#            maxb = b
#
#print maxa,maxb,maxn
#            


## Problem 26
#cyclens = []
#for x in range(1,1000):
#    remainders = []
#    for cyclen in range(1,999):
#        rem = 10**cyclen%x
#        if rem in remainders:
#            cyclens.append(len(remainders[remainders.index(rem):]))
#            print cyclens[-1], x
#            break;
#        else:
#            remainders.append(rem)
#        if cyclen==998:
#            print x, "??????????????"
#print max(cyclens)
#print cyclens.index(max(cyclens))+1 #forgot to add one for a minute


## problem 25
## silly mistake I made for a bit, using 10**1000 instead of 10*999
#
#fib = [1,1]
#i=2
#while fib[-1]<10**999:
#    fib.append(sum(fib))
#    fib.pop(0)
#    i+=1
#    if i<13:
#        print fib,i
#print i


## Problem 24
#
#from scipy.misc import factorial
#
#number = 1000000
#
#digits = [0,1,2,3,4,5,6,7,8,9]
#end = []
#
#for x in range(9,0,-1):
#    i=0
#    xfact = factorial(x)
#    while xfact<number:
#        number = number-xfact
#        i+=1
#    print end, digits, number, xfact, x, i
#    end.append(digits.pop(i))
#print end, digits, number, xfact, x, i




## Problem 23
## This solution has TERRIBLE runtime; takes about five minutes.
## Probably the best improvement would be to restrict the search for y-abundant[i]
## to utilize the fact that abundant is sorted.
#
#def properdivisors(num):
#    divisors = [1]
#    for x in range(2,num//2+1):
#        if num%x==0:
#            divisors.append(x)
#    return divisors
#
#abundant = []
#
#for x in range(1,28123):
#    if x%1000==0:
#        print "Checking abundant numbers at ",x
#    if sum(properdivisors(x))>x:
#        abundant.append(x)
#
#total = 0
#
#for y in range(28123):
#    if y%1000==0:
#        print "Checking sums at ",y
#    i=0
#    sumfound = False
#    while(abundant[i]< y//2+1 and not sumfound):
#        if i%100==9:
#            print "Checking {} for sums through {}".format(y,abundant[i])
#        if y-abundant[i] in abundant:
#            #print abundant[i],sum(properdivisors(abundant[i]))
#            #print y-abundant[i],sum(properdivisors(y-abundant[i]))
#            #print y
#            sumfound = True
#        i+=1
#    if not sumfound:
#        total +=y
#
#print total
    


## Problem 21
#
#def properdivisors(num):
#    divisors = [1]
#    for x in range(2,num//2+1):
#        if num%x==0:
#            divisors.append(x)
#    return divisors
#
#amicablelist = []
#
#for i in range(1,10001):
#    #print i,d
#    d = sum(properdivisors(i))
#    if sum(properdivisors(d))==i and i!=d:
#        print d,i
#        amicablelist.append(i)
#
#print sum(amicablelist)


#==============================================================================
# # Problem 20
# num = 1
# for x in range(1,101):
#     num = num*x
# num = str(num)
# total = 0
# for digit in num:
#     total+= int(digit)
# print total
#==============================================================================


#==============================================================================
# # Problem 16
# 
# num = str(2**1000)
# total = 0
# for digit in num:
#     total+= int(digit)
# print total
#==============================================================================


#==============================================================================
# #Problem 15
# # easy because it simplifies to "compute 40 choose 20"
# # took a while because I forgot how for loops are indexed >.<
# 
# twen = 1
# for x in range(1,21):
#     twen = twen*x
# fort = 1
# for x in range(21,41):
#     fort = fort*x
#     print fort
# print fort/twen
#==============================================================================

#==============================================================================
# #Problem 14
# 
# # dumb problem here; forgot to start my loop at 1 and it looped forever.
# # I expected this to need more optimization.
# 
# def nextcollatz(number):
#     if number%2==0:
#         return number/2
#     else:
#         return 3*number+1
# 
# t0 = time.time()
# maxlen = 0
# for x in range(1,1000000):
#     y=x
#     coll = [y]
#     while y!=1:
#         if np.random.random()<.0000001:
#             print "Working on {} at time {}".format(x,time.time()-t0)
#         y=nextcollatz(y)
#         coll.append(y)
#     if len(coll)>maxlen:
#         maxlen = len(coll)
#         print x, maxlen
# 
#==============================================================================

#==============================================================================
# #Problem 12
# 
# powersoftwo = [2**x for x in range(50)]
# powersofthree = [3**x for x in range(50)]
# 
# def listfactors(number):
#     factors =[]
#     for x in range(1,(number+2)//2):
#         if number%x==0:
#             factors.append(x)
#     factors.append(number)
#     return factors
#             
# #This took a while because my factor checking wasn't fast enough.
# #Eventually I realized I could estimate the number of factors of triangular numbers
# #By their indices. Once I realized that I only had to check factors of the
# #Indices which improved time to the square root of what it had been previously.
# 
# t0=time.time()
# found = False
# counter = 64
# again = False
# while(not found):
#     counter+=1
#     if len(listfactors(counter))>22 and len(listfactors(counter+1))>22:
#         print counter
#         triangle= counter*(counter+1)/2
#         fact = listfactors(triangle)
#         if len(fact)>200:
#             print triangle, len(fact), counter, time.time()-t0
#         found = len(fact)>500
#         del fact           
# print triangle
#  
#==============================================================================

'''
#problem 10

def is_not_divis(x,stuff):
    for item in stuff:
        if x%item == 0:
            return False
        elif item**2 > x:
            return True
    return True

import time
t0 = time.time()
primes = [2,3,5]
nextnum = 7
while(nextnum<2000000):
    if is_not_divis(nextnum,primes):
        primes.append(nextnum)
    nextnum+=2

import numpy
print "Python sum:\t",sum(primes)
print "Numpy sum:\t",numpy.sum(primes, dtype=numpy.int64)
print len(primes)
print 2000000/numpy.log(2000000)
'''


'''problem 9
for x in range(1,900):
    for y in range(x,1000-x):
        if x**2+y**2 == (1000-x-y)**2:
            print x*y*(1000-x-y)
            break
'''

'''problem 8
bignum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

maxprod = 1
for x in range(len(bignum)-13):
    prod = 1
    for y in range(13):
        prod = prod*int(bignum[x+y])
    if prod > maxprod:
        maxprod = prod
print maxprod
'''

'''Problem 7
def is_not_divis(x,stuff):
    for item in stuff:
        if x%item== 0:
            return False
    return True

primes = [2,3,5,7,11,13,17,19,23]
nextnum = 29
while(len(primes)<10001):
    if is_not_divis(nextnum,primes):
        primes.append(nextnum)
    nextnum+=2

print primes[10000]
'''


'''Problem 6
sumsquare = 0
squaresum = 0
for x in range(101):
    sumsquare+=x**2
    squaresum+=x
print squaresum**2 - sumsquare
'''

'''#Problem 5: stupid solution

def is_divis(x,stuff):
    for item in stuff:
        if x%item!= 0:
            return False
    return True
    
x=2520
while(not is_divis(x,range(1,21))):
    x+=2520

print x

#Problem 5: too fancy
prod = 20
for x in range(19,1,-1):
    print x, prod
    if prod%x==0:
        print "already included"
        pass
    elif x%(prod%x) != 0 or prod%x==1:
        print "new!"
        prod = prod*x
    else:
        print "Will acquire later"
print prod
'''


'''Problem 4:
def is_palindrome(number):
    number = str(number)
    if len(number)<=1:
        return True
    else:
        return number[0]==number[-1] and is_palindrome(number[1:-1])

print is_palindrome(77),is_palindrome(123547),is_palindrome(101)

maxpal = 0
for x in range(999,100,-1):
    for y in range(999,100,-1):
        if is_palindrome(x*y):
            if x*y>maxpal:
                maxpal =  x*y
            break
print maxpal

'''

"""Problem 1:
sum=0
for x in range(1000):
    if x%3==0 or x%5==0:
        sum+=x

print sum
#"""

'''Problem 2:

sum=0
fib=[1,1]
while(fib[-1]<=4000000):
    fib.append(fib[-1]+fib[-2])
fib.pop()
for x in fib:
    if x%2==0:
        sum+=x
print sum
'''

'''Problem 3:
number = 600851475143
factor = 2
greatestfactor = 0

while factor<=number:
    while(number%factor==0):
        print number, factor, number%factor,number/factor
        number = number/factor
        greatestfactor = factor
    factor+=1
print greatestfactor
'''