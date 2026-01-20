"""
Given a list of package weights, find grouping such that all packages are in one of 4 groups and
all groups are the same weight, and minimize primarily the # of packages in the 1st group and
secondarily the QE (product) of the 1st group's weights
"""

from math import prod
from itertools import combinations

# -----
# solve
# -----

def solve(filepath):
    """
    Given the path of a file containing valid input, return the solution
    """
    with open(filepath, encoding='utf-8') as file:
        # NOTE: set is simple to use and possible because all weights in input are unique.
        # for an input with duplicate weights, implementation would be trickier
        weights = set(map(int, file))

    group_weight = sum(weights) // 4
    found_valid = False
    best_qe_found = 0
    for i in range(1, len(weights) // 4 + 1):
        for combo in combinations(weights, i):
            if sum(combo) == group_weight:
                remaining_3_4_weights = weights.difference(combo)
                for j in range(i, len(remaining_3_4_weights) // 3 + 1):
                    for combo_2 in combinations(remaining_3_4_weights, j):
                        if sum(combo_2) == group_weight:
                            remaining_1_2_weights = remaining_3_4_weights.difference(combo_2)
                            for k in range(j, len(remaining_1_2_weights) // 2 + 1):
                                for combo_3 in combinations(remaining_1_2_weights, k):
                                    if sum(combo_3) == group_weight:
                                        found_valid = True
                                        if not best_qe_found or prod(combo) < best_qe_found:
                                            best_qe_found = prod(combo)
                                        break
                                if found_valid:
                                    break
                    if found_valid:
                        break
        if found_valid:
            break
    return best_qe_found

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('sample_input'))
    print(solve('input'))
