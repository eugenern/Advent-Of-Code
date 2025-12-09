"""
Given a list of ranges of fresh ingredient IDs, count how many ingredient IDs in total are fresh
"""

# -------
# imports
# -------

import sys

# -------
# globals
# -------

raw_fresh_ranges = []
merged_fresh_ranges = []

# ---------------
# count_all_fresh
# ---------------

def count_all_fresh():
    """
    assuming fresh ranges have already been merged appropriately,
    return total number of fresh ingredient IDs possible
    """
    return sum(fresh_range[1] - fresh_range[0] + 1 for fresh_range in merged_fresh_ranges)

# ------------
# merge_ranges
# ------------

def merge_ranges():
    """
    sort and merge the raw fresh ranges to be non-overlapping
    """
    raw_fresh_ranges.sort(key=lambda x: x[0])
    for fresh_range in raw_fresh_ranges:
        if not merged_fresh_ranges or fresh_range[0] > merged_fresh_ranges[-1][1]:
            merged_fresh_ranges.append(fresh_range)
        else:
            merged_fresh_ranges[-1][1] = max(merged_fresh_ranges[-1][1], fresh_range[1])

# ----------
# read_range
# ----------

def read_range(string):
    """
    get lower and upper bounds of the range
    """
    return list(map(int, string.split('-')))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        if not line.rstrip():
            merge_ranges()
            writer.write(str(count_all_fresh()))
            break
        raw_fresh_ranges.append(read_range(line))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
