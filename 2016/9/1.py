"""
Given a compressed sequence of characters, find the length of the decompressed file
"""

# -------
# imports
# -------

import sys

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    # doesn't use regex; try reimplementing with regex and see if it's a better soln
    for line in reader:
        final = ''
        p = line.partition('(')
        while p[1] != '':
            final += p[0]
            p = p[2].partition('x')
            num_chars = int(p[0])
            p = p[2].partition(')')
            reps = int(p[0])
            final += p[2][:num_chars] * reps
            p = p[2][num_chars:].partition('(')
        final += p[0]
        writer.write(str(len(final)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
