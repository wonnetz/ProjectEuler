"""
Coded by Wonnetz Phanthavong
Title: Smallest Multiple
Difficulty Rating: 5%
Question:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
# This was the first method that I tried, brute force. The method worked to find 2520, but it ran too long to find
# the LCM of the numbers between 1 to 20. Thus, we shall try a different method, by looking at the theory of LCMs.
count = 1
num = 20
while not (count % 21 == 0):
    count = 1
    num = num + 1
    for k in range(1,21):
        if num % k == 0:
            count += 1
print(num)
"""
import numpy as np

primes = []
uniqueP = []
p = 2

# This loop allows us to get the prime factorization of the numbers between 1 and 20
for n in range(1, 21):
    while n > 1:
        while n % p == 0:
            primes.append(p)
            n /= p
        p += 1
    # Finds the unique primes in the list
    for k in range(len(primes)):
        if not (primes[k] in uniqueP):
            uniqueP.append(primes[k])
    p = 2
    primes = []

# Creates a 2-Dimensional Array which will house the unique primes and their max occurances
array = np.zeros((2, len(uniqueP)), dtype=int)
for i in range(0, len(uniqueP)):
    array[0][i] = uniqueP[i]

# Counts how many times a prime occurs
for j in range(0, len(uniqueP)):
    for n in range(1, 21):
        while n > 1:
            while n % p == 0:
                primes.append(p)
                n /= p
            p += 1
        p = 2
        count = primes.count(array[0][j])
        primes = []
        if count > array[1][j]:
            array[1][j] = count
print(array)
print("The first row represents the unique primes that occur between 1 and 20.")
print("The second row indicates how many times the unique prime occurs in the prime factorizations between 1 and 20.")
print(" ")
# Multiples all the entries of the array to give us our desired result
LCM = 1
for i in range(0, len(uniqueP)):
    LCM *= (array[0][i] ** array[1][i])
print("The smallest possible number that is evenly divisible by all numbers between 1 and 20, ")
print("i.e., the LCM, is given by " + str(LCM))




