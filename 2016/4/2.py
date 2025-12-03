"""
Given a list of rooms, find the sector ID of the room that stores North Pole objects
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
    name = re.sub('-', '', name)
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

# -------
# decrypt
# -------

def decrypt(name, sector_id):
    """
    given the encrypted room name and sector id, decrypt the name
    """
    name = re.sub('-', ' ', name)
    rotation = sector_id % 26
    def shift_letter(matchobj):
        return chr((ord(matchobj.group(0)) - 97 + rotation) % 26 + 97)
    return re.sub('[a-z]', shift_letter, name)

# ----
# read
# ----

def read(string):
    """
    get the name, sector id, and checksum from a room string
    """
    return (re.match(r'([a-z\-]+)-\d', string).group(1),
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
    # calling read() 5 times inefficient, oh well
    writer.write(str(
        [
            read(line)[1] for line in reader
            if 'northpole' in decrypt(read(line)[0], read(line)[1])
            and check(read(line)[0], read(line)[2])
        ]
        ))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
