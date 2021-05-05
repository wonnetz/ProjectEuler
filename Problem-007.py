"""
Coded by Wonnetz Phanthavong
Title: 10001st Prime
Difficulty Rating: 5%
Question:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
# To solve this we shall first use Fermat's Little Theorem, to give us canidates which are 'probably' prime.
# https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
# Then we will brute force check to see if these numbers are indeed prime by dividing them with smaller numbers.


primes = [2]
n = 3
while not (len(primes) == 10001):
    a = 2
    a = a ** (n-1) - 1
    if a % n == 0:
        for i in range(2, n):
            if n % i == 0:
                break
            elif i == n-1:
                primes.append(n)
                break
    n += 2  # We increment by 2, because we know that the only even prime number is 2.
print(max(primes))

"""
Output: 104743
"""
