"""
Coded by Wonnetz Phanthavong
Title: Sum Square Difference
Difficulty Rating: 5%
Question:
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# Finds the sum of the squares of the first one hundred natural numbers
sumSq = 0
for i in range(1,101):
    sumSq += i ** 2

# Finds the square of the sum of the first one hundred natural numbers
Sqsum = 0
for i in range(1, 101):
    Sqsum += i
Sqsum = Sqsum ** 2

Diff = Sqsum - sumSq
print(Diff)

"""
Output: 25164150
"""