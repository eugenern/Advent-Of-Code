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

    min_count = len(column)
    for char in set(column):
        if column.count(char) < min_count:
            real_char = char
            min_count = column.count(char)
    return real_char

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """

    message = ''
    messages = [line for line in reader]
    for column in zip(*messages):
        next_char = least_freq(column)
        message += next_char
    writer.write(message)

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
