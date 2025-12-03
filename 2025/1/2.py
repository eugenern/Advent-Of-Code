"""
Given instructions of the format [RL]\\d+ and a dial with positions 0-99 starting at 50,
determine how many times while running through the instructions the dial passes through 0
"""

# -------
# imports
# -------

import sys

# ------------------------
# calculate pass through 0
# ------------------------

def calculate_pass_through_0(cur_pos, direction, steps):
    """
    given dial's current position and a new instruction,
    calculate number of times dial passes through 0
    """
    # to calculate initial pass through: check if going R would take dial past 99
    # or if going L would take dial to/past 0 (assuming it's not starting at 0 already)
    initial_pass_through = 1 if (direction == 'R' and cur_pos + steps > 99) \
        or (direction == 'L' and cur_pos > 0 and cur_pos - steps <= 0) else 0

    # to calculate additional pass throughs:
    # example: cur_pos = 90, dir = R. steps 0-9 no pass through; 10+ has initial pass through;
    # 10-109 has only one pass through; 110+ has excess pass throughs
    # if dir = L: steps 0-89 no pass through; 90+ has initial pass through;
    # 90-189 has only one pass through; 190+ has excess pass throughs
    # therefore, if R, calc using max(0, steps - 10); if L calc using max(0, steps - 90)
    excess_pass_throughs = (max(0, steps - ((100 - cur_pos) if direction == 'R' else cur_pos))) // 100
    return initial_pass_through + excess_pass_throughs

# -------------
# update result
# -------------

def update_result(cur_pos, times_at_0, direction, steps):
    """
    given dial's current position and a new instruction,
    find how many times dial points to 0 during rotation
    """
    # we no longer add 1 to times_at_0 for ending an instruction at 0
    # since that gets included in the calculation of pass throughs
    new_pos = (cur_pos + (1 if direction == 'R' else -1) * steps) % 100

    times_at_0 += calculate_pass_through_0(cur_pos, direction, steps)
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
