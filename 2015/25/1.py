"""
Given the code for row 1, column 1, find the code requested by the machine
"""

# -----
# parse
# -----

def parse(line):
    """
    Given a line of input, return the instruction and its arguments
    """
    tokens = line.split()
    row = int(tokens[tokens.index('row') + 1].rstrip(',.'))
    col = int(tokens[tokens.index('column') + 1].rstrip(',.'))
    return row, col

# -----
# solve
# -----

def solve(filepath):
    """
    Given the path of a file containing valid input, return the solution
    """
    with open(filepath, encoding='utf-8') as file:
        row, col = parse(file.read())

    # i spent way too much time deriving this formula from the table of diagonal values
    iterations = (row ** 2 + col ** 2 + 2 * row * col - 3 * row - col + 2) // 2

    # i asked gemini how to simplify the process of multiplying by x and modding by y millions of times
    initial = 20151125
    mul = 252533
    mod = 33554393
    return initial % mod * pow(mul, iterations - 1, mod) % mod

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('input'))
