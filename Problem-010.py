"""
Coded by Wonnetz Phanthavong
Title: Summation of Primes
Difficulty Rating: 5%
Question:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
# We use the Sieve of Eratosthenes to find all the prime numbers up to two million.
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math
primes = []

# Creates a list of integers up until two million
for i in range(2, 2000001):
    primes.append(i)

# Removes certain values of the list according to the Sieve of Eratosthenes
for j in range(0, math.ceil(math.sqrt(2000000))):
    index = primes[j]
    if not primes[j] == 0:
        while j + index < 1999999:  # 1999999
            primes[j + index] = 0
            index += primes[j]

print("The sum of the prime numbers less than two million is as follows: " + str(int(math.fsum(primes))))

"""
Output: The sum of the prime numbers less than two million is as follows: 142913828922
"""
