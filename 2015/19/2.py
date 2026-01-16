"""
Given a list of molecule replacements and a molecule, return the fewest replacements needed to turn
e into the medicine molecule
"""

# -----------------
# parse replacement
# -----------------

def parse_replacement(line):
    """
    Given a line describing a molecule replacement, return the old and new
    """
    parts = line.partition(' => ')
    return parts[0], parts[2]

# -----
# solve
# -----

def solve(filepath):
    """
    Given the path of a file containing valid input, return the solution
    """
    reverse_replacements = {}
    goal = 'no molecule'
    with open(filepath, encoding='utf-8') as file:
        replacements_done = False
        for line in file:
            clean_line = line.rstrip()
            if not clean_line:
                replacements_done = True

            if not replacements_done:
                old, new = parse_replacement(clean_line)
                reverse_replacements[new] = old
            else:
                goal = clean_line

    # for k, v in reverse_replacements.items():
    #     print(f'{k}: {v}')
    steps = 0
    while goal != 'e':
        # print(goal)
        for new, old in reverse_replacements.items():
            # print(f'\t{new} -> {old}')
            if old == 'e':
                if goal == new:
                    steps += 1
                    goal = old
                    break
                continue
            while new in goal:
                # print(f'\t\t{new} is in {goal}')
                i = occs = 0
                while i < len(goal):
                    # print(f'\t\tsearching from index {i}. substr is {goal[i:i + len(new)]}')
                    if goal[i:i + len(new)] == new:
                        occs += 1
                        i += len(new)
                    else:
                        i += 1
                # print(f'\t\tfound {occs} occs')
                goal = goal.replace(new, old)
                steps += occs
                # print(f'\t\tgoal is now {goal}, steps {steps}')

    return steps

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('sample_input'))
    print(solve('input'))
