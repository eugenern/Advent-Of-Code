"""
Given instructions of the format [UDLR]+ separated by a newline, determine the bathroom code.
"""

# -------
# imports
# -------

import sys

# --------------
# move_to_button
# --------------

def move_to_button(button, moves):
    """
    get next button given previous button and movements
    """
    for m in moves:
        if m == 'U' and button > 3:
            button -= 3
        elif m == 'D' and button < 7:
            button += 3
        elif m == 'L' and button % 3 != 1:
            button -= 1
        elif m == 'R' and button % 3 != 0:
            button += 1
    return button

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    button = 5
    for line in reader:
        button = move_to_button(button, line)
        writer.write(str(button))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
