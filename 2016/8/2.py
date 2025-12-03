"""
Given a list of instructions for the screen, show what the screen displays
"""

# -------
# imports
# -------

import sys

# ------
# screen
# ------

# initially all pixels are off
screen = [[False] * 50 for i in range(6)]

# ---------
# make_rect
# ---------

def make_rect(w, h):
    """
    turn on all pixels in a w x h rectangle in the top left corner
    """
    for i in range(h):
        for j in range(w):
            screen[i][j] = True

# ------
# rotate
# ------

def rotate(direction, loc, mag):
    """
    shift a certain row/column by a certain amount
    """
    if direction == 'row':
        width = len(screen[loc])
        mag %= width
        screen[loc] = screen[loc][(width - mag):] + screen[loc][:(width - mag)]
    else:
        height = len(screen)
        mag %= height
        temp = [screen[i][loc] for i in range(height)]
        for i in range(height):
            screen[i][loc] = temp[i - mag]

# ----
# read
# ----

def read(line):
    """
    figure out line's instruction and relevant parameters
    """
    words = line.split()
    if words[0] == 'rect':
        dims = words[1].split('x')
        return (words[0], int(dims[0]), int(dims[1]))
    return (words[1], int(words[2][2:]), int(words[4]))

# -------------
# print_letters
# -------------

def print_letters():
    """
    print out the screen's display
    """
    for i in range(len(screen)):
        disp = ['#' if x else '.' for x in screen[i]]
        print(*disp, sep='')

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    writer a writer
    """
    for line in reader:
        instr = read(line)
        if instr[0] == 'rect':
            make_rect(instr[1], instr[2])
        else:
            rotate(*instr)

    print_letters()

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
