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
        if m == "U":
            if button % 10 == 3:
                button -= 2
            elif 4 % button != 0 and 5 % (button - 4) != 0:
                button -= 4
        elif button != 13:
            if m == "L" and 10 % button != 0:
                button -= 1
            elif button != 9:
                if m == "D":
                    if button % 10 == 1:
                        button += 2
                    elif button < 9 and button != 5:
                        button += 4
                if m == "R" and button not in [1, 4, 12]:
                    button += 1
    return button

# --------
# convert_button
# --------

def convert_button(button):
    """
    convert button number to appropriate string
    """
    if button > 9:
        return chr(button + 55)
    return str(button)

# ----
# read
# ----

def read(string):
    """
    get movements to next button
    """
    return [string[n:n+1] for n in range(len(string))]

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
        moves = read(line)
        button = move_to_button(button, moves)
        to_write = convert_button(button)
        writer.write(to_write)

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
