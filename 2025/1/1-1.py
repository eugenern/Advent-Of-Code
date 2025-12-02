"""
Given instructions of the format [RL]\\d+ and a dial with positions 0-99 starting at 50,
determine how many times while running through the instructions the dial points to 0
"""

# -------
# imports
# -------

import sys

# -------------
# update result
# -------------

def update_result(cur_pos, times_at_0, direction, steps):
    """
    given dial's current position and a new instruction, find dial's new position
    and update if dial is at 0
    """
    new_pos = (cur_pos + (1 if direction == 'R' else -1) * steps) % 100
    if not new_pos:
        times_at_0 += 1

    return new_pos, times_at_0

# ----
# read
# ----

def read(string):
    """
    get direction and number of steps
    """
    return string[0], int(string[1:])

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    times_at_0 = 0
    cur_pos = 50
    for line in reader:
        direction, steps = read(line)
        cur_pos, times_at_0 = update_result(cur_pos, times_at_0, direction, steps)

    writer.write(str(times_at_0))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
