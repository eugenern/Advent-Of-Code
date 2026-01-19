"""
Given a program of instructions, find the final value of register b
"""

# -----
# parse
# -----

def parse(line):
    """
    Given a line of input, return the instruction and its arguments
    """
    tokens = line.split()
    instr = tokens[0]
    args = []
    for arg in tokens[1:]:
        clean_arg = arg.rstrip(',')
        if clean_arg.isalpha():
            args.append(0 if clean_arg == 'a' else 1)
        else:
            args.append(int(clean_arg.lstrip('+')))
    return instr, args

# -----
# solve
# -----

def solve(filepath):
    """
    Given the path of a file containing valid input, return the solution
    """
    pc = 0
    registers = [0, 0]
    with open(filepath, encoding='utf-8') as file:
        instrs = list(map(parse, file))

    while 0 <= pc < len(instrs):
        instr, args = instrs[pc]
        # print(instr, args)
        if instr == 'hlf':
            registers[args[0]] //= 2
        elif instr == 'tpl':
            registers[args[0]] *= 3
        elif instr == 'inc':
            registers[args[0]] += 1
        elif instr == 'jmp':
            pc += args[0]
        elif instr == 'jie':
            pc += args[1] if not registers[args[0]] % 2 else 1
        elif instr == 'jio':
            pc += args[1] if registers[args[0]] == 1 else 1
        if instr[0] != 'j':
            pc += 1

    return registers[1]

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('input'))
