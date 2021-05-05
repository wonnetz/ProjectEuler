"""
Coded by Wonnetz Phanthavong
Title: Special Pythagorean Triplet
Difficulty Rating: 5%
Question:
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

dummy = 1
c = 9

# The first loop checks the numbers that are less than c to find a
# The second loop checks the numbers that are between a and b
while dummy:
    for i in range(1, c):
        a = i
        a2 = a ** 2
        for j in range(a, c):
            b = j
            b2 = b ** 2
            # Checks to see if a,b, and c are a Pythagorean Triple
            if math.sqrt(a2 + b2) == c:
                if a + b + c == 1000:
                    dummy = 0
                    print("The unique Pythagorean Triple for which a + b + c = 1000 is given as ")
                    print(a * b * c)
    c += 1

"""
Output: The unique Pythagorean Triple for which a + b + c = 1000 is given as 
        31875000
"""
