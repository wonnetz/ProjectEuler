"""
Coded by Wonnetz Phanthavong
Title: Number Letter counts
Difficulty Rating: 5%
Question:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is
in compliance with British usage.
"""

# Function accounts for every case of numbers between 1 and 999 (inclusive)
def special(n):
    if n >= 100:
        first = n // 100  # Gets the first digit of the number
        tot = special(first) + 7  # Adds the character number in 'hundred'
        n -= first * 100
        if n == 0:
            return tot
        else:
            return tot + special(n) + 3  # Performs the function on the tens digits while also counting 'and'
    elif 19 < n < 100:
        first = n // 10
        n -= first * 10
        if first == 2 or first == 3 or first == 8 or first == 9:
            return 6 + special(n)
        elif first == 4 or first == 5 or first == 6:
            return 5 + special(n)
        elif first == 7:
            return 7 + special(n)

    elif 10 <= n <= 19:
        n = n % 10
        if n == 0:
            return 3
        elif n == 1 or n == 2:
            return 6
        elif n == 5 or n == 6:
            return 7
        elif n == 3 or n == 4 or n == 8 or n == 9:
            return 8
        elif n == 7:
            return 9
    elif n == 0:
        return 0
    elif n == 1 or n == 2 or n == 6:
        return 3
    elif n == 3 or n == 7 or n == 8:
        return 5
    elif n == 4 or n == 5 or n == 9:
        return 4


total_char = 0
for n in range(0, 1000):
    total_char += special(n)
print(total_char + 11)  # Where the '+11' comes from the 'one thousand'

"""
Output: 21124
"""