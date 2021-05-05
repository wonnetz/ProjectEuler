"""
Coded by Wonnetz Phanthavong
Title: Largest Prime Factor
Difficulty Rating: 5%
Question:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

primes = []
n = 600851475143
p = 3

while n > 1:
    while n % p == 0:
        primes.append(p)
        n /= p
    p +=1
print(max(primes))

"""
Output: 6857
"""
