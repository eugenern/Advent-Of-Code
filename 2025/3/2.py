"""
Given banks of battery joltages, find max joltage of each bank and sum the maxes
"""

# -------
# imports
# -------

import sys

# ------------
# find_joltage
# ------------

def find_joltage(digits):
    """
    find the max value possible from concatenating 12 digits in the order found in bank
    """
    earliest_possible_ind = 0
    total = 0
    for i in range(11, -1, -1):
        digit = max(digits[earliest_possible_ind : len(digits) - i])
        total += digit * 10 ** i
        for j in range(earliest_possible_ind, len(digits) - i):
            if digits[j] == digit:
                earliest_possible_ind = j + 1
                break

    return total

# ----
# read
# ----

def read(string):
    """
    convert string of digits to list of ints
    """
    return list(map(int, string))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(str(sum(find_joltage(read(line.rstrip())) for line in reader)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
