r"""
Given instructions of the format [RL]\d+ separated by a comma and space,
determine how far away the first repeated location is in taxicab geometry.
"""

# -------
# imports
# -------

import sys

# -----
# cache
# -----

visited = {0: set([0])} # latitude: longitudes

# -------------------
# update the position
# -------------------

def update_pos(state, turn, num):
    """
    update state based on turn and num while keeping track of visited states
    """
    if turn == 'R':
        state[0] = (state[0] + 1) % 4
    elif turn == 'L':
        state[0] = (state[0] - 1) % 4

    if state[0] % 2: # going E or W
        for _ in range(num):
            state[2] += (state[0] - 2)
            if state[2] in visited[state[1]]:
                return state, True

            visited[state[1]].add(state[2])
    else: # going N or S
        for _ in range(num):
            state[1] += (state[0] - 1)
            if state[1] in visited and state[2] in visited[state[1]]:
                return state, True

            if state[1] not in visited:
                visited[state[1]] = set()
            visited[state[1]].add(state[2])

    return state, False

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
            state, done = update_pos(state, turn, num)
            if done:
                break
        writer.write(str(abs(state[1]) + abs(state[2])))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
