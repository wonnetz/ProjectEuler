"""
Coded by Wonnetz Phanthavong
Title: Longest Collatz Sequence
Difficulty Rating: 5%
Question:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def collatz(n):
    if n == 1:
        return int(n)
    elif n % 2 == 0:
        return int(n / 2)
    else:
        return int((3*n) + 1)


longest_chain = []
for i in range(1, 1000000):
    logic = 1
    chain = []
    chain.append(i)
    n = i
    while logic:
        n = collatz(n)
        chain.append(n)
        if len(chain) > len(longest_chain):
            longest_chain = chain
        if n == 1:
            logic = 0
print(longest_chain[0])

"""
Output: 837799
"""