import numpy as np
import matplotlib.pyplot as plt

def bracelet(a,b,n):
    if not (0 <= a < 10**n):
        if a < 0:
            a = a % 10
        if a > 10^n:
            a = a % 10^n
    #if not isinstance(a, int):
    #    a = round(a)
    if not (0 <= b < 10**n):
        if b < 0:
            b = b % 10
        if b > 10^n:
            b = b % 10^n
    #if not isinstance(b, int):
    #    b = round(b)

    cycle = [a, b]
    while True:
        num = (cycle[-1] + cycle[-2]) % 10**n
        cycle.append(num)

        if cycle[-2:] == [a, b]:
            break
            
    length = len(cycle)
    return cycle, length

n = 2 #number of digits in the elements of the bracelet. Would be 1 in the original problem
a = 2.5 #first number
b = -6 #second number

print(bracelet(a, b, n))
