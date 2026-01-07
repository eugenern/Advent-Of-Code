"""
Given a list of distances between locations, calculate the total distance of the shortest route
to visit every location exactly once
"""

# -------
# imports
# -------

import sys
from itertools import permutations

# --------------
# form_dist_dict
# --------------

def form_dist_dict(reader):
    """
    Given list of distances between locations, for a dict mapping start loc to a dict that maps
    dest locs to distances
    """
    dist_dict = {}
    for line in reader:
        words = line.split()
        loc_1, loc_2, dist = words[0], words[2], int(words[-1])
        if loc_1 not in dist_dict:
            dist_dict[loc_1] = {}
        if loc_2 not in dist_dict:
            dist_dict[loc_2] = {}
        dist_dict[loc_1][loc_2] = dist
        dist_dict[loc_2][loc_1] = dist

    return dist_dict

# -----
# solve
# -----

def solve(reader):
    """
    Use distances between locations to find shortest route to visit every location once
    """
    # idea: form a dict start loc -> dict dest loc -> distance
    # remember to set dict item in both directions

    # also, during the search (BFS or DFS?) keep track of least total distance found so far
    # and cut a search short if the distance becomes too far

    # alternate idea: instead of BFS or DFS, iterate thru all permutations of all locations
    # i guess that would involve a lot of recalculations tho

    # another idea: instead of 8! permutations, fix a starting loc and for each of the 7!
    # permutations of routes from there, subtract the greatest distance in the path

    dist_dict = form_dist_dict(reader)
    # for k, v in dist_dict.items():
    #     print(k)
    #     for k1, v1 in v.items():
    #         print(f'\tdest {k1} dist {v1}')

    best_found = sum(sum(v.values()) for v in dist_dict.values()) // 2
    for route in permutations(dist_dict.keys()):
        route_dist = 0
        for i, loc in enumerate(route[:-1]):
            route_dist += dist_dict[loc][route[i + 1]]
            if route_dist >= best_found:
                break
        if route_dist < best_found:
            best_found = route_dist

    return best_found

# ----
# main
# ----

if __name__ == "__main__":
    print(solve(sys.stdin))
