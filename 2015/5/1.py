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
    vowel_set = set(('a', 'e', 'i', 'o', 'u'))
    double = False
    forbidden = set(('ab', 'cd', 'pq', 'xy'))
    for i, c in enumerate(string):
        if c in vowel_set:
            vowel_count += 1
        if i < len(string) - 1:
            if c == string[i + 1]:
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
    writer.write(str(len([line for line in reader if is_nice(line.rstrip())])))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
