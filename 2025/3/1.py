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
    find the max value possible from concatenating two digits in the order found in bank
    """
    tens = max(digits[:-1])
    ind = digits.index(tens)
    ones = max(digits[ind + 1 : ])
    return tens * 10 + ones

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
