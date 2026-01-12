"""
Given a list of seating pairs and their happiness modifiers, return the total happiness
modification of the optimal seating arrangement
"""

from itertools import permutations

# -----
# parse
# -----

def parse(line):
    """
    Given a seating pair and its happiness modifier, return a key, value pair for the happy dict
    """
    tokens = line.rstrip('.\n').split()
    attendee, neighbor, happiness = tokens[0], tokens[-1], (1 if tokens[2] == 'gain' else -1) * int(tokens[3])
    return attendee, neighbor, happiness

# -----
# solve
# -----

def solve(filepath):
    """
    Given the path of a file containing valid input, return the solution
    """
    happy = {}
    with open(filepath, encoding='utf-8') as file:
        for line in file:
            attendee, neighbor, happiness = parse(line)
            if attendee not in happy:
                happy[attendee] = {}
            happy[attendee][neighbor] = happiness

    return max(sum(happy[a][p[(i + 1) % len(p)]] + happy[a][p[(i - 1) % len(p)]] for i, a in enumerate(p)) for p in permutations(happy.keys()))

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('sample_input'))
    print(solve('input'))
