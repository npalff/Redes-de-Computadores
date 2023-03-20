
import math
import sys

def comb(n,k):
    return ((math.factorial(n))/(math.factorial(k)*math.factorial(n-k)))

def binDistribution(n,k,p,q):
    return comb(n,k)*(p**k)*(q**(n-k))

def binDistribution_atMost(n,p,q,maxUsers):
    probFinal = 0.0
    print("--------------------\n")
    for i in range(maxUsers+1):
        probFinal = probFinal + binDistribution(n,i,p,q)
        print(probFinal)
        print("\n")
    print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
    return probFinal

n = 35
pX = 0.1
maxUsers = 35

qX = 1-pX

print("O valor é:")
print(1 - binDistribution_atMost(n,pX,qX,maxUsers))
print("\n\n")


