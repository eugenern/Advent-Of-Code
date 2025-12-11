"""
Given a list of devices and which devices each one outputs to,
find how many paths lead from 'svr' to 'out' while passing through 'dac' and 'fft'
"""

# -------
# imports
# -------

import sys

# ----------------
# search for paths
# ----------------

def search_for_paths(flows, from_dev, to_dev, cutoffs):
    """
    Given a mapping from device to destinations, find all paths from 'svr' to 'out'
    that pass through 'dac' and 'fft'

    observations so far from trying to solve:
    w/ BFS, svr->fft is very common
    w/ BFS, svr->dac is very hard to find
    we can't search the entire space of possible paths, need to prune somehow
    using DFS, paths from svr to out are very common
    ok, installed graphviz and checked graph to help with pruning
    """
    paths = 0
    initial_seen = []

    initial_state = (from_dev, initial_seen)
    fringe = [initial_state]
    while fringe:
        cur_dev, cur_seen = fringe.pop()

        if cur_dev == to_dev:
            paths += 1
            # if not paths % 50:
            #     print(paths)
            continue

        # if paths > 2579:
        #     print(f'curdev {cur_dev} and curseen {cur_seen}')

        for dest in flows[cur_dev]:
            if dest == 'out' and to_dev != 'out':
                print(f'HUHHH found "out" when looking thru dev {cur_dev} and seen {cur_seen}')
                continue
            if dest not in cutoffs:
                new_seen = cur_seen + [dest]
                fringe.append((dest, new_seen))

    return paths

# ----
# read
# ----

def read(string):
    """
    get a device and the devices it outputs to
    """
    device, outputs = (parts := string.split(':'))[0], parts[1].split()
    return device, outputs

# -----
# solve
# -----

def solve(reader):
    """
    reader a reader
    """
    flows = dict(map(read, reader))
    # sets of cutoff nodes formed via manual inspection of graph visualization
    no_to_fft = {'vjr', 'crz', 'lfa', 'cqs', 'csd', 'prl', 'qys', 'ebd', 'pao', 'ehw', 'cri', 'rnb',
                 'dak', 'cox', 'nfk', 'kgk', 'vwa', 'wko', 'fzw', 'jzl', 'jkz', 'psa', 'ekw'}
    no_to_dac = {'eva', 'hst', 'nzv', 'vvp', 'srk', 'khw', 'hsb', 'dgk', 'nqa', 'pin', 'diq', 'yrr',
                 'vrh', 'xey', 'qeq', 'svs', 'wvz'}
    print(search_for_paths(flows, 'svr', 'fft', no_to_fft)
          * search_for_paths(flows, 'fft', 'dac', no_to_dac)
          * search_for_paths(flows, 'dac', 'out', set()))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
