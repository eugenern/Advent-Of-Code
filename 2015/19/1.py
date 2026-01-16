"""
Given a list of molecule replacements and a molecule, return how many resulting molecules are
possible after one replacement
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
    to_modify = 'no molecule'
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
                to_modify = clean_line

    molecules = set()
    i = 0
    while i < len(to_modify):
        elem_end = i + 1
        while elem_end < len(to_modify) and to_modify[elem_end].islower():
            elem_end += 1
        to_replace = to_modify[i:elem_end]
        if to_replace in replacements:
            for new in replacements[to_replace]:
                molecules.add(f'{to_modify[:i]}{new}{to_modify[elem_end:]}')
        i = elem_end

    return len(molecules)

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('input'))
