"""
Given a list of microchip and bot instructions,
multiply the values of one chip in each of the outputs 0, 1, and 2
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys

# -----------
# global vars
# -----------

# hardcoding in the number of bots
bots = [set() for i in range(210)]
# lists should be in format [give low to, bot or output, give high to, bot or output]
give_tos = [[] for i in range(210)]
# hardcoding in the number of outputs
outputs = [[] for i in range(21)]

# ---
# run
# ---

def run():
    """
    transfer chips according to the instructions until no bot has 2 chips
    """
    full_bots = list(filter(lambda x: len(x) == 2, bots))
    while full_bots:
        for chips in full_bots:
            bot = bots.index(chips)
            if give_tos[bot][1] == 'bot':
                bots[give_tos[bot][0]].add(min(chips))
            else:
                outputs[give_tos[bot][0]].append(min(chips))
            if give_tos[bot][3] == 'bot':
                bots[give_tos[bot][2]].add(max(chips))
            else:
                outputs[give_tos[bot][2]].append(max(chips))
            bots[bot].clear()
        full_bots = list(filter(lambda x: len(x) == 2, bots))

# ---------
# add_instr
# ---------

def add_instr(instr):
    """
    interpret an instruction and add its values to the relevant list
    """
    words = instr.split()
    if words[0] == 'bot':
        # add to bot instr list
        give_tos[int(words[1])] = [int(words[6]), words[5], int(words[11]), words[10]]
    else:
        # give bot in bot list the chip
        bots[int(words[5])].add(int(words[1]))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    # go line by line to build up an instruction list of lists
    # where index is bot and list shows who to give chips
    # also fill a list of bots and their chip slots
    for line in reader:
        add_instr(line)
    run()
    writer.write(str(outputs[0][0] * outputs[1][0] * outputs[2][0]))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
