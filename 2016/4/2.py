"""
Given a list of rooms, find the sector ID of the room that stores North Pole objects
"""

# -------
# imports
# -------

import sys
import re

# -------
# decrypt
# -------

def decrypt(name, sector_id):
    """
    given the encrypted room name and sector id, decrypt the name according to shift cipher
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
    get the name and sector id from a room string
    """
    return (re.match(r'([a-z\-]+)-\d', string).group(1),
            int(re.search('[0-9]+', string).group(0)))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    # note: the problem statement doesn't explicitly state
    # that 'northpole' should be in the real name;
    # without that info, solution would require listing out all real names
    # (optionally filtering out decoy rooms) and manually inspecting them
    writer.write(str(next(
        id for (name, id) in map(read, reader) if 'northpole' in decrypt(name, id)
        )))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
