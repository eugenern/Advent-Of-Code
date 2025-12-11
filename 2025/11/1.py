"""
Given a list of devices and which devices each one outputs to,
find how many paths lead from 'you' to 'out'

i'm guessing we have to keep track of path during search to make sure next destination doesn't create cycle
NOTE: upon visualizing the graph, it turns out there probably aren't any cycles to worry about
"""

# -------
# imports
# -------

import sys

# ----------------
# search for paths
# ----------------

def search_for_paths(flows):
    """
    Given a mapping from device to destinations, find all paths from 'you' to 'out'
    """
    paths = 0
    initial_seen = set()
    inital_dev = 'you'
    initial_state = (inital_dev, initial_seen)
    fringe = [initial_state]
    while fringe:
        cur_dev, cur_seen = fringe[0]
        del fringe[0]

        if cur_dev == 'out':
            paths += 1
            continue

        for dest in flows[cur_dev]:
            if dest not in cur_seen:
                new_seen = cur_seen | {dest}
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
    print(search_for_paths(flows))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin)
