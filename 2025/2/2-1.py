"""
Given ranges of product IDs, find all invalid IDs within all ranges and return sum
"""

# -------
# imports
# -------

import sys

# ----------------------
# find_invalids_in_range
# ----------------------

def find_invalids_in_range(lo, hi):
    """
    search range for all invalid IDs
    """
    for i in range(lo, hi + 1):
        i_str = str(i)
        num_digits = len(i_str)
        if not num_digits % 2 and i_str[ : num_digits // 2] == i_str[num_digits // 2 : ]:
            yield i

# ----
# read
# ----

def read(string):
    """
    get ranges and yield as lo, hi
    """
    range_strs = string.split(',')
    for range_str in range_strs:
        num_strs = range_str.split('-')
        yield int(num_strs[0]), int(num_strs[1])

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    invalids_sum = 0
    for line in reader:
        for lo, hi in read(line):
            invalids_sum += sum(find_invalids_in_range(lo, hi))

    writer.write(str(invalids_sum))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
