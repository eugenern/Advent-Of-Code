"""
Given a list of reindeer speeds and flying/rest periods, find who goes the farthest after 2503s
"""

# -----
# parse
# -----

def parse(line):
    """
    Given a line describing a reindeer, return the reindeer's speed, flying period, and rest period
    """
    tokens = line.rstrip('.\n').split()
    fly_pos, rest_pos = tokens.index('fly'), tokens.index('rest')
    reindeer, speed, fly_time, rest_time = tokens[0], int(tokens[fly_pos + 1]), int(tokens[fly_pos + 4]), int(tokens[rest_pos + 2])
    return reindeer, (speed, fly_time, rest_time)

# -----
# solve
# -----

def solve(filepath, end_time):
    """
    Given the path of a file containing valid input, return the solution
    """
    with open(filepath, encoding='utf-8') as file:
        reindeer_stats = dict(map(parse, file))

    fastest_reindeer, max_dist_found = [], 0
    for reindeer, (speed, fly_time, rest_time) in reindeer_stats.items():
        cycle_len = fly_time + rest_time
        full_cycles = end_time // cycle_len
        full_cycles_dist = full_cycles * speed * fly_time
        partial_cycle = end_time % cycle_len
        partial_cycle_dist = min(partial_cycle, fly_time) * speed
        dist = full_cycles_dist + partial_cycle_dist
        if dist >= max_dist_found:
            if dist == max_dist_found:
                fastest_reindeer.append(reindeer)
            else:
                fastest_reindeer = [reindeer]
            max_dist_found = dist

    return fastest_reindeer, max_dist_found

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('sample_input', 1000))
    print(solve('input', 2503))
