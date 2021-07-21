"""
Coded by Wonnetz Phanthavong
Title: Maximum Path Sum 1
Difficulty Rating: 5%
Question:
Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
There are 15 rows here
"""


# Turns the triangle into a 2d array
with open('problem18triangle.txt') as f:
    w = [int(x) for x in next(f).split()] # reads first line
    array = []
    array.append(w)
    for line in f: # reads the rest of the lines
        array.append([int(x) for x in line.split()])


# We start at the bottom of the triangle and add upwards.
# This was a clever trick that I found while researching binary trees and their paths.
for i in range(13, -1, -1):
    for j in range(0, len(array[i])):
        sum1 = array[i][j] + array[i+1][j]
        sum2 = array[i][j] + array[i+1][j+1]
        if sum1 > sum2:
            array[i][j] = sum1
        else:
            array[i][j] = sum2
print(array[0][0])

"""
Output: 1074
"""
