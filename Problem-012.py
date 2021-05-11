"""
Coded by Wonnetz Phanthavong
Title: Highly Divisible Triangular Number
Difficulty Rating: 5%
Question:
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""
from functools import reduce

# Returns the factors of a number
def factors(n):
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))

n = 0
count = 0
tri = 0
while count < 500:
    count = 0
    n += 1
    tri += n
    count = len(factors(tri))
print("The triangle number with over 500 divisors is the " + str(n) + "th triangle number which is " + str(tri) + ".")

"""
Output: The triangle number with over 500 divisors is the 12375th triangle number which is 76576500.
"""