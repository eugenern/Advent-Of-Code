"""
Given a tachyon manifold diagram, calculate how many times the beam will split
"""

# -------
# imports
# -------

import sys

# ----
# read
# ----

def read(string):
    """
    get a set of the locations of each splitter in the row
    """
    splitters = set()
    for i, c in enumerate(string):
        if c == '^' or c == 'S':
            splitters.add(i)
    return splitters

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    beams = dict.fromkeys(read(reader.readline()), 1)
    for line in reader:
        splitters = read(line)
        new_beams = {}
        for beam, timelines in beams.items():
            if beam in splitters:
                new_beams[beam - 1] = new_beams.get(beam - 1, 0) + timelines
                new_beams[beam + 1] = new_beams.get(beam + 1, 0) + timelines
            else:
                new_beams[beam] = new_beams.get(beam, 0) + timelines
        beams = new_beams

    writer.write(str(sum(beams.values())))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
