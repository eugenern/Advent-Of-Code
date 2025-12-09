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
        for j in range(2, num_digits + 1):
            if not num_digits % j and \
                all(
                    i_str[ : num_digits // j] == \
                        i_str[k * num_digits // j : (k + 1) * num_digits // j] \
                            for k in range(1, j)
                ):
                yield i
                break

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
