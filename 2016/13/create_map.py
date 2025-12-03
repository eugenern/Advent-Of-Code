#!/usr/bin/env python3

# input
FAV_NUM = 1364

# 100x100 is just a guess for the maximum area needed;
# may not allow globally optimal solution to be found
area = [['.'] * 100 for i in range(100)]

for y in range(len(area)):
    for x in range(len(area[0])):
        if bin(x*x + 3*x + 2*x*y + y + y*y + FAV_NUM).count('1') % 2:
            area[y][x] = '#'

# goal
area[39][31] = '*'

for row in area:
    for loc in row:
        print(loc, end='')
    print()
