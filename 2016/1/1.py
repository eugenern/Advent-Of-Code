r"""
Given instructions of the format [RL]\d+ separated by a comma and space,
determine how far away the destination is in taxicab geometry.
"""

# -------
# imports
# -------

import sys

# -------------------
# update the position
# -------------------

def update_pos(state, turn, num):
    """
    update state based on turn and num
    """
    if turn == 'R':
        state[0] = (state[0] + 1) % 4
    elif turn == 'L':
        state[0] = (state[0] - 1) % 4

    if state[0] % 2: # going E or W
        state[2] += (state[0] - 2) * num
    else: # going N or S
        state[1] += (state[0] - 1) * num

    return state

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
    for line in reader:
        state = [0, 0, 0] # facing (0=N, 1=E, 2=S, 3=W), units S, units E
        for instruction in line.split(', '):
            turn, num = read(instruction)
            state = update_pos(state, turn, num)
        writer.write(str(abs(state[1]) + abs(state[2])))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
