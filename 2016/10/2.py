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
bots = [set() for _ in range(210)]
# lists should be in format [bot or output, give low to, bot or output, give high to]
give_tos = [[] for _ in range(210)]
# hardcoding in the number of outputs
outputs = [[] for _ in range(21)]

# ---
# run
# ---

def run():
    """
    transfer chips according to the instructions until no bot has 2 chips
    """
    while any(len(bot) > 1 for bot in bots):
        for i, bot in enumerate(bots):
            if len(bot) > 1:
                lo_dest_type, lo_dest_ind, hi_dest_type, hi_dest_ind = give_tos[i]
                if lo_dest_type == 'bot':
                    bots[lo_dest_ind].add(min(bot))
                else:
                    outputs[lo_dest_ind].append(min(bot))
                if hi_dest_type == 'bot':
                    bots[hi_dest_ind].add(max(bot))
                else:
                    outputs[hi_dest_ind].append(max(bot))
                bot.clear()

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
        give_tos[int(words[1])] = [words[5], int(words[6]), words[10], int(words[11])]
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
