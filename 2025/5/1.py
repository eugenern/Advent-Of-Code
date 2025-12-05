"""
Given a list of ranges of fresh ingredient IDs and a list of available ingredient IDs,
count how many available ingredient IDs are fresh
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

# --------
# is_fresh
# --------

def is_fresh(ing_id):
    """
    given an ingredient id, determine whether it is fresh
    """
    return any(fresh_range[0] <= ing_id <= fresh_range[1] for fresh_range in merged_fresh_ranges)

# ----------
# read_range
# ----------

def read_range(string):
    """
    get lower and upper bounds of the range
    """
    return list(map(read_id, string.split('-')))

# -------
# read_id
# -------

def read_id(string):
    """
    get an ingredient ID
    """
    return int(string)

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    count = 0
    ranges_done = False
    for line in reader:
        if not line.rstrip():
            merge_ranges()
            ranges_done = True
        elif not ranges_done:
            raw_fresh_ranges.append(read_range(line))
        else:
            if is_fresh(read_id(line)):
                count += 1

    writer.write(str(count))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
