"""
Given a list of ingredients and their properties per teaspoon, find the best score possible for 100
teaspoons of ingredients that add up to 500 calories
"""

from math import prod

# ---------------------------------------------
# combos
# Source - https://stackoverflow.com/a/69140296
# Posted by delver
# Retrieved 2026-01-13, License - CC BY-SA 4.0
# ---------------------------------------------

def combos(nbins, qty):
    bins = [0]*nbins
    bins[0] = qty #starting bin quantities
    while True:
        yield bins
        if bins[-1] == qty:
            return #last combo, we're done!
        #leftmost bar movement (inner loop)
        if bins[0] > 0:
            bins[0] -= 1
            bins[1] += 1
        else:
            #bump next bar in nested loops
            #i.e., find first nonzero entry, and split it
            nz = 1
            while bins[nz] == 0:
                nz +=1
            bins[0]=bins[nz]-1
            bins[nz+1] += 1
            bins[nz] = 0

# ---------------
# calculate score
# ---------------

def calc_score(props, amounts):
    """
    Given the properties and amounts of each ingredient, calculate the score
    """
    # ex: butter cap -1 dur -2 fla 6 tex 3
    #     cinna cap 2 dur 3 fla -2 tex -1
    #     amount 44 butter 56 cinna
    #     => max(0, 44 * -1 + 56 * 2) * ...
    if sum(props[i][-1] * a for i, a in enumerate(amounts)) != 500:
        return -1
    return prod(max(0, sum(t)) for t in zip(*[[a * p for p in props[i][:-1]] for i, a in enumerate(amounts)]))

# -----
# parse
# -----

def parse(line):
    """
    Given a line describing an ingredient, return the ingredient's properties
    """
    tokens = line.rstrip('.\n').split()
    cap, dur, fla, tex, cal = (int(tokens[tokens.index(prop) + 1].rstrip(',')) for prop in ('capacity', 'durability', 'flavor', 'texture', 'calories'))
    return (cap, dur, fla, tex, cal)

# -----
# solve
# -----

def solve(filepath, teaspoons):
    """
    Given the path of a file containing valid input, return the solution
    """
    with open(filepath, encoding='utf-8') as file:
        props = tuple(map(parse, file))

    return max(calc_score(props, combo) for combo in combos(len(props), teaspoons))

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('sample_input', 100))
    print(solve('input', 100))
