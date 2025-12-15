"""
Given a list of strings, determine how many are considered nice
"""

# -------
# imports
# -------

import sys

# -------
# is_nice
# -------

def is_nice(string):
    """
    given a string, determine whether it is considered nice
    """
    vowel_count = 0
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    double = False
    forbidden = {'ab', 'cd', 'pq', 'xy'}
    for i, c in enumerate(string):
        if vowel_count < 3 and c in vowel_set:
            vowel_count += 1
        if i < len(string) - 1:
            if not double and c == string[i + 1]:
                double = True
            if c + string[i + 1] in forbidden:
                return False

    return vowel_count >= 3 and double

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(str(sum(map(is_nice, map(str.rstrip, reader)))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
