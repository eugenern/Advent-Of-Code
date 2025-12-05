"""
Given a repeated but corrupted message, recover the message
"""

# -------
# imports
# -------

import sys

# ----------
# least_freq
# ----------

def least_freq(column):
    """
    find the value with the lowest frequency in the tuple
    """
    letter_freqs = {}
    for c in column:
        letter_freqs[c] = letter_freqs.get(c, 0) + 1

    return sorted(letter_freqs.items(), key=lambda x: x[1])[0][0]

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(''.join(map(least_freq, zip(*reader))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
