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
        while p[1]:
            final += p[0]
            p = p[2].partition('x')
            num_chars = int(p[0])
            p = p[2].partition(')')
            reps = int(p[0])
            final += p[2][:num_chars] * reps
            p = p[2][num_chars:].partition('(')
        final += p[0]
        writer.write(str(len(final)))

# -----------------
# solve_only_length
# -----------------

def solve_only_length(reader, writer):
    """
    same algorithm as solve() except only tracks length instead of building the decompressed string
    Theoretically should be faster and more memory-efficient
    """
    total = 0
    file = reader.read()
    ind = -1
    while (ind := ind + 1) < len(file):
        if file[ind] != '(':
            total += 1
            continue
        num_chars = 0
        while file[(ind := ind + 1)] != 'x':
            num_chars *= 10
            num_chars += int(file[ind])
        reps = 0
        while file[(ind := ind + 1)] != ')':
            reps *= 10
            reps += int(file[ind])
        total += num_chars * reps
        ind += num_chars

    writer.write(str(total))

# ----
# main
# ----

if __name__ == "__main__":
    solve_only_length(sys.stdin, sys.stdout)
