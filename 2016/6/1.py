"""
Given a repeated but corrupted message, recover the message
"""

# -------
# imports
# -------

import sys

# ---------
# most_freq
# ---------

def most_freq(column):
    """
    find the value with the highest frequency in the tuple
    """
    letter_freqs = {}
    letter_found = column[0]
    for c in column:
        letter_freqs[c] = letter_freqs.get(c, 0) + 1
        if letter_freqs[c] > letter_freqs[letter_found]:
            letter_found = c
    return letter_found

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(''.join(map(most_freq, zip(*reader))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
