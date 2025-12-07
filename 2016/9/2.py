"""
Given a compressed sequence of characters, find the length of the decompressed file
"""

# -------
# imports
# -------

import sys
import re

# -------
# globals
# -------

prog = re.compile(r'\((\d+)x(\d+)\)')

# ----------
# decompress
# ----------

def decompress(string, i = 0, endpos = 0):
    """
    given a file and the start and end points to consider,
    recursively calculate decompressed length according to markers
    """
    if not endpos:
        endpos = len(string)

    count = 0
    while (match := prog.search(string, i, endpos)):
        num_chars, reps = map(int, match.groups())
        count += match.start() - i + decompress(string, match.end(), match.end() + num_chars) * reps
        i = match.end() + num_chars
    count += endpos - i
    return count

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    # NOTE: DON'T try to construct the decompressed sequence; use MATH to figure out the length
    for line in reader:
        writer.write(str(decompress(line)))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
