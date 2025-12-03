"""
Given a list of rooms, sum up the sector IDs of the real rooms
"""

# -------
# imports
# -------

import sys
import re

# -----
# check
# -----

def check(name, checksum):
    """
    given a room name and the checksum, check whether the room is real
    """
    all_letters = {}
    for c in name:
        if c in all_letters:
            all_letters[c] += 1
        else:
            all_letters[c] = 0
    count = 0
    for letter_freq in \
        sorted(sorted(all_letters.items(), key=lambda x: x[0]), key=lambda x: x[1], reverse=True):
        if letter_freq[0] != checksum[count]:
            return False
        if count == 4:
            return True
        count += 1

# ----
# read
# ----

def read(string):
    """
    get the name, sector id, and checksum from a room string
    """
    string = re.sub('-', '', string)
    return (re.match('[a-z]+', string).group(0),
            int(re.search('[0-9]+', string).group(0)),
            re.search(r'\[([a-z]+)\]', string).group(1))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    # calling read() 3 times inefficient, oh well
    writer.write(str(
        sum([read(line)[1] for line in reader if check(read(line)[0], read(line)[2])])
        ))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
