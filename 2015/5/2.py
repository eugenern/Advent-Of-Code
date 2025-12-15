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
    repeated_pair = sandwich = False
    for i, c in enumerate(string):
        if not repeated_pair and i < len(string) - 3:
            pair = c + string[i + 1]
            if pair in string[i + 2 : ]:
                repeated_pair = True
        if not sandwich and i < len(string) - 2 and c == string[i + 2]:
            sandwich = True
        if repeated_pair and sandwich:
            return True

    return False

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
