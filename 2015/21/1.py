"""
Given an item shop and boss stats, find the cheapest set of items to defeat the boss
"""

from itertools import product, combinations, chain

# ----------
# battle sim
# ----------

def battle(player_stats, boss_stats):
    """
    Given a player and a boss, determine whether the player wins the battle
    """
    player_hp, player_dmg, player_arm = player_stats
    boss_hp, boss_dmg, boss_arm = boss_stats
    player_turns = player_hp // max(1, boss_dmg - player_arm)
    boss_turns = boss_hp // max(1, player_dmg - boss_arm)
    # print(f'player dies in {player_turns} turns, boss {boss_turns}')
    return player_turns >= boss_turns

# ---------------
# parse item shop
# ---------------

def parse_item_shop(filepath):
    """
    Given a file, return lists of weapons, armor, and rings with their costs and stats
    """
    # each item is a tuple of 3 ints
    items = ([], [], [])
    with open(filepath, encoding='utf-8') as file:
        status = -1 # 0 = weapons, 1 = armor, 2 = rings
        for line in file:
            clean_line = line.rstrip()
            if not clean_line:
                continue
            if ':' in clean_line:
                status += 1
                continue
            tokens = clean_line.split()
            items[status].append(tuple(map(int, tokens[-3:])))

    return items

# -----
# parse
# -----

def parse(filepath):
    """
    Given a filepath to a file containing boss stats, return the stats
    """
    with open(filepath, encoding='utf-8') as file:
        lines = file.readlines()

    return tuple(map(int, (line.split()[-1] for line in lines)))

# -----
# solve
# -----

def solve(filepath, player_stats):
    """
    Given the path of a file containing valid input, return the solution
    """
    weapons, armor, rings = parse_item_shop('item_shop')
    # player may equip no armor and/or 0-2 rings. so 0 armor is an option
    armor.append((0, 0, 0))
    boss_stats = parse(filepath)

    print('weapons', *weapons, sep='\n')
    print('armor', *armor, sep='\n')
    print('rings', *rings, sep='\n')
    print('boss stats', boss_stats)
    best_found = sum(sum(item[0] for item in items) for items in (weapons, armor, rings))
    for items in product(weapons, armor, chain.from_iterable(combinations(rings, r) for r in range(3))):
        flattened = items[:2] + items[2]
        total_cost, total_dmg, total_arm = map(sum, zip(*flattened))
        if battle(tuple(map(sum, zip(player_stats, (0, total_dmg, total_arm)))), boss_stats) and total_cost < best_found:
            best_found = total_cost
    return best_found

# ----
# main
# ----

if __name__ == "__main__":
    sample_player = (8, 5, 5)
    print(f'Player wins sample battle? {battle(sample_player, parse('sample_input'))}')
    player = (100, 0, 0)
    print(solve('input', player))
