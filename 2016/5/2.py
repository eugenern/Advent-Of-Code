"""
Given a door ID, construct the door's password
according to the algorithm described on the AoC website
"""

# -------
# imports
# -------

import sys
from hashlib import md5

# -------------
# find_password
# -------------

def find_password(door_id):
    """
    apply md5 hash to door_id + integer index and form the door's password
    """
    index = 0
    password = '--------'

    while '-' in password:
        m = md5((door_id + str(index)).encode()).hexdigest()
        if all(c == '0' for c in m[:5]) and (pos := int(m[5], 16)) < 8 and password[pos] == '-':
            password = password[:pos] + m[6] + password[pos + 1:]
        index += 1

    return password

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        writer.write(find_password(line))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
