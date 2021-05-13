"""
Coded by Wonnetz Phanthavong
Title: Lattice Paths
Difficulty Rating: 5%
Question:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
# Another way of formulating this problem is as a Binomial Coefficient Problem.
# https://en.wikipedia.org/wiki/Binomial_coefficient
# Given that there are 20 grid points,
# how many different ways can we move at each grid point, given 2 options, i.e., left and right.
# With this in mind, we see that there are 40 possible choices in total, but we would like to know
# how many different ways we can arrange these possible choices.
# Which is where the Binomial Coefficient formula comes in to play
# Using the Binomial Coefficient formula, we see that this is simply '40 choose 20'
# The traditional way of computing the Binomial Coefficient formula is through the usage of factorials,
# but this can use up a lot of memory. Therefore, we've opted to use the Gamma Function instead.

import math

paths = round(math.exp(math.log(math.gamma(41)) - math.log(math.gamma(21)) - math.log(math.gamma(21))))
print(paths)

"""
Output: 137846528820
"""