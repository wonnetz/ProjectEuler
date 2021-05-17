"""
Coded by Wonnetz Phanthavong
Title: Power Digit Sums
Difficulty Rating: 5%
Question:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""
num = 2 ** 1000
digits = []
# This loop records the last digit, appends it to the list, and then removes the last digit
while num > 0:
    digits.append(num % 10)
    num //= 10
print(sum(digits))

"""
Output: 1366
"""