"""
Given instructions for connecting wires in a circuit, determine what signal is provided to wire 'a'
"""

# -------
# imports
# -------

import sys
from itertools import repeat

# ----
# read
# ----

def read(string):
    """
    determine values, operands, input and output wires
    """
    # what should format of return value be?
    # idea: operand, input wires, output wire
    parts = string.split()
    out_wire = parts[-1]
    op = ''
    in_wires = []
    for part in parts[:-2]:
        if part.isupper():
            op = part
        elif part.isdecimal():
            in_wires.append(int(part))
        else:
            in_wires.append(part)

    return op, frozenset(in_wires), out_wire

# -----
# solve
# -----

def solve(reader):
    """
    connect all the wires and set values
    """
    # issue: instructions are not in order of circuit flow
    # idea: create a dict mapping inputs to instructions
    # and a set tracking which wires are defined (and thus can be used as inputs)

    wire_vals = {}
    input_to_instrs = {}
    inputs_to_run = set()
    defined_inputs = set()
    for line in reader:
        op, in_wires, out_wire = read(line)
        defined_inputs.update(filter(lambda x: isinstance(x, int), in_wires))
        if in_wires not in input_to_instrs:
            input_to_instrs[in_wires] = []
        input_to_instrs[in_wires].append((op, out_wire))
        if all(map(isinstance, in_wires, repeat(int))):
            inputs_to_run.add(in_wires)

    # for k, v in input_to_instrs.items():
    #     print(k)
    #     for i in v:
    #         print(f'\t{i}')

    while inputs_to_run:
        input_to_run = inputs_to_run.pop()
        if input_to_run in input_to_instrs:
            in_lst = list(input_to_run)
            for op, out_wire in input_to_instrs[input_to_run]:
                if all(map(isinstance, in_lst, repeat(int))):
                    wire_vals[out_wire] = in_lst[0]
                elif op == 'AND':
                    v0 = wire_vals[in_lst[0]] if isinstance(in_lst[0], str) else in_lst[0]
                    v1 = wire_vals[in_lst[1]] if isinstance(in_lst[1], str) else in_lst[1]
                    wire_vals[out_wire] = v0 & v1
                elif op == 'OR':
                    v0 = wire_vals[in_lst[0]] if isinstance(in_lst[0], str) else in_lst[0]
                    v1 = wire_vals[in_lst[1]] if isinstance(in_lst[1], str) else in_lst[1]
                    wire_vals[out_wire] = v0 | v1
                elif op.endswith('SHIFT'):
                    str_in, int_in = (in_lst[0], in_lst[1]) if isinstance(in_lst[0], str) else (in_lst[1], in_lst[0])
                    wire_vals[out_wire] = (wire_vals[str_in] << int_in) if op[0] == 'L' else (wire_vals[str_in] >> int_in)
                elif op == 'NOT':
                    wire_vals[out_wire] = ~(wire_vals[in_lst[0]]) & 0xFFFF
                else:
                    wire_vals[out_wire] = wire_vals[in_lst[0]]

                if out_wire == 'a':
                    return wire_vals[out_wire]

                inputs_to_run.add(frozenset([out_wire]))
                inputs_to_run.update(frozenset((out_wire, defined_input)) for defined_input in defined_inputs)
                defined_inputs.add(out_wire)

    # for k, v in wire_vals.items():
    #     print(k, v)
    return 0

# ----
# main
# ----

if __name__ == "__main__":
    print(solve(sys.stdin))
