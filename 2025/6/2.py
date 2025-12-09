"""
Given a cephalopod math worksheet with numbers in cephalopod notation,
find the grand total sum of all the answers to the individual problems
"""

# -------
# imports
# -------

import sys
from math import prod

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    total = 0
    nums = []
    op = sum
    lines = list(reader)
    # starting from left vs right doesn't matter
    for i in range(len((lines[-1]))):
        op_char = (col := list(row[i].strip() for row in lines))[-1]
        if any(col):
            if op_char:
                op = sum if op_char == '+' else prod
            num = 0
            for digit in col[:-1]:
                if digit:
                    num *= 10
                    num += int(digit)
            nums.append(num)
        else:
            total += op(nums)
            nums = []
    total += op(nums)

    writer.write(str(total))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
