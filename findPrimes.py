# -*- coding: utf-8 -*-
# Script to print the list of primes in a given range

'''
Returns true, if the given number is prime
'''
def is_prime(x):
    if x == 1 or x == 2 :
        return True
    if x % 2 == 0 :
        return False
    
    for i in range(3, int(math.sqrt(x))+1, 2) :
        if x % i == 0 :
            return False
    return True
    
#Driver Program
lower, upper = map(int, input().split())
for i in range(lower, upper) :
    if is_prime(i) :
        print(i)
