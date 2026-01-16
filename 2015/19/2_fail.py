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
    replacements = {}
    goal = 'no molecule'
    with open(filepath, encoding='utf-8') as file:
        replacements_done = False
        for line in file:
            clean_line = line.rstrip()
            if not clean_line:
                replacements_done = True

            if not replacements_done:
                old, new = parse_replacement(clean_line)
                replacements[old] = replacements.get(old, []) + [new]
            else:
                goal = clean_line

    # format for the BFS: track steps, current molecule
    fringe = [(0, 'e')]
    seen = set()
    cur_steps = longest = 0
    while fringe:
        steps, cur_mol = fringe[0]
        del fringe[0]
        if cur_mol in seen:
            continue
        seen.add(cur_mol)
        if steps > cur_steps:
            print(f'steps {steps}')
            cur_steps = steps
        if len(cur_mol) > longest:
            print(f'longest so far {cur_mol} w/ len {len(cur_mol)}')
            longest = len(cur_mol)
        if cur_mol == goal:
            return steps
        i = 0
        while i < len(cur_mol):
            elem_end = i + 1
            while elem_end < len(cur_mol) and cur_mol[elem_end].islower():
                elem_end += 1
            to_replace = cur_mol[i:elem_end]
            if to_replace in replacements:
                for new in replacements[to_replace]:
                    fringe.append((steps + 1, f'{cur_mol[:i]}{new}{cur_mol[elem_end:]}'))
            i = elem_end

    return -1

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('sample_input'))
    print(solve('input'))
