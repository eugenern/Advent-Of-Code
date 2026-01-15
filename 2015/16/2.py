"""
Given a list of Aunt Sues and some of their characteristics, find which Sue sent the gift
"""

gift = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''

# -----
# parse
# -----

def parse(line):
    """
    Given a line describing an Aunt Sue, return her ID and characteristics
    """
    tokens = line.rstrip('.\n').split()
    sue_id = int(tokens[1].rstrip(':'))
    chars = {}
    i = 2
    while i < len(tokens):
        chars[tokens[i].rstrip(':')] = int(tokens[i + 1].rstrip(','))
        i += 2
    return sue_id, chars

# -----
# solve
# -----

def solve(filepath):
    """
    Given the path of a file containing valid input, return the solution
    """
    with open(filepath, encoding='utf-8') as file:
        sues = dict(map(parse, file))

    gift_lines = gift.split('\n')
    gift_chars = {(parts := gift_line.partition(': '))[0]: int(parts[2]) for gift_line in gift_lines}

    for sue, chars in sues.items():
        valid = True
        for char, amount in chars.items():
            if char in {'cats', 'trees'}:
                if amount <= gift_chars[char]:
                    valid = False
                    break
            elif char in {'pomeranians', 'goldfish'}:
                if amount >= gift_chars[char]:
                    valid = False
                    break
            else:
                if amount != gift_chars[char]:
                    valid = False
                    break
        if valid:
            return sue

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('input'))
