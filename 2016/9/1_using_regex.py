"""
Given a compressed sequence of characters, find the length of the decompressed file
"""

# -------
# imports
# -------

import sys
import re

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        final = ''
        prog = re.compile(r'\((\d+)x(\d+)\)')
        while (match := prog.search(line)):
            final += line[:match.start()]
            num_chars, reps = map(int, match.groups())
            final += line[match.end():(match.end() + num_chars)] * reps
            line = line[(match.end() + num_chars):]
        final += line
        writer.write(str(len(final)))

# -----------------
# solve_only_length
# -----------------

def solve_only_length(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        # this is silly, but one could see the decompressed length as the length of the file
        # plus lengths of extra reps minus lengths of markers
        total = len(line)
        ind = 0
        prog = re.compile(r'\((\d+)x(\d+)\)')
        while (match := prog.search(line, ind)):
            num_chars, reps = map(int, match.groups())
            total += num_chars * (reps - 1) - len(match.group())
            ind = match.end() + num_chars
        writer.write(str(total))

# ----
# main
# ----

if __name__ == "__main__":
    solve_only_length(sys.stdin, sys.stdout)
