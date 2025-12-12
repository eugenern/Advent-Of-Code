"""
Given indicator light diagrams, button wiring schematics, and joltage requirements,
calculate the fewest total button presses required to reach correct joltage levels

This solution uses systems of linear equations to find valid button press combinations
At first I tried using sympy but failed. scipy had a simpler solution
"""

# -------
# imports
# -------

import sys
# from itertools import product
from numpy import ones
from scipy.optimize import linprog
# from sympy import symbols, linsolve, Matrix

# ---------
# configure
# ---------

def configure(machine):
    """
    Given a machine's joltage requirements and button wiring schematics,
    calculate and return the least number of button presses needed to reach correct joltage
    """
    jolts, buttons = machine
    num_buttons = len(buttons)
    matrix = [[0] * num_buttons for _ in range(len(jolts))]
    for i, button in enumerate(buttons):
        for to_inc in button:
            matrix[to_inc][i] = 1

    # syms_list = list(chr(97 + i) for i in range(num_buttons))
    # syms = symbols(' '.join(syms_list))
    # system = Matrix(matrix), jolts
    # vector = linsolve(system, *syms)
    # soln = list(vector)[0]
    # params = [syms[i] for i in range(num_buttons) if str(syms[i]) in str(soln)]
    # min_presses = sum(jolts) if params else sum(soln)
    # for combination in product(range(num_buttons), repeat=len(params)):
    #     sym_vals = {}
    #     for i, var in enumerate(combination):
    #         sym_vals[params[i]] = var
    #     if (new_sum := sum(soln.subs(sym_vals))) < min_presses and all(term >= 0 for term in soln.subs(sym_vals)):
    #         min_presses = new_sum

    # print(jolts, min_presses)
    # return min_presses

    c = ones(num_buttons)
    soln = linprog(c, A_eq=matrix, b_eq=jolts, integrality=c)
    if any(not val.is_integer() for val in soln.x):
        print('ALERTTTTTTTTTTTTTTTTTT fractions')
    if soln.status:
        print('NOOOOOOOOOOOOOOOOOOOOO status', soln.message)
    print(soln.x, soln.fun)

    return soln.fun

# ----
# read
# ----

def read(string):
    """
    get joltage requirements and button wiring schematic
    """
    jolt_str, buttons_strs = (machine := string.split())[-1], machine[1:-1]
    jolt = tuple(map(int, jolt_str[1:-1].split(',')))
    buttons = tuple(tuple(map(int, buttons_str[1:-1].split(','))) for buttons_str in buttons_strs)
    return jolt, buttons

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    """
    print(sum(map(configure, map(read, reader))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
