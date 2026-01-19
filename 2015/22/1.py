"""
Given boss stats, determine the least amount of mana the player can use to defeat the boss
"""

# ------------
# apply effect
# ------------

def apply_effect(state):
    """
    Given the current state of the battle, apply any active effects and update their timers
    """
    if state['shield_timer']:
        state['shield_timer'] -= 1
        if not state['shield_timer']:
            state['player_armor'] = 0
    if state['poison_timer']:
        state['boss_hp'] -= 3
        state['poison_timer'] -= 1
    if state['recharge_timer']:
        state['player_mana'] += 101
        state['recharge_timer'] -= 1

# -------------------------
# run player and boss turns
# -------------------------

def run_turns(state, boss_dmg):
    """
    Given the current state of the battle, apply any active effects, then for each of the 5 existing
    spells, cast them, apply any active effects, and run the boss's turn

    Note: for each possible spell if at any time the battle ends, stop that battle and return state
    """
    # first, apply any active effects and decrement their timers
    apply_effect(state)
    if state['boss_hp'] <= 0:
        return [state]

    new_states = []
    # existing spells: Magic Missile, Drain, Shield, Poison, Recharge
    if state['player_mana'] >= 53:
        mm_state = state.copy()
        mm_state['player_mana'] -= 53
        mm_state['mana_spent'] += 53
        mm_state['boss_hp'] -= 4
        new_states.append(mm_state)
    if state['player_mana'] >= 73:
        d_state = state.copy()
        d_state['player_mana'] -= 73
        d_state['mana_spent'] += 73
        d_state['player_hp'] += 2
        d_state['boss_hp'] -= 2
        new_states.append(d_state)
    if state['player_mana'] >= 113 and not state['shield_timer']:
        s_state = state.copy()
        s_state['player_mana'] -= 113
        s_state['mana_spent'] += 113
        s_state['shield_timer'] = 6
        s_state['player_armor'] = 7
        new_states.append(s_state)
    if state['player_mana'] >= 173 and not state['poison_timer']:
        p_state = state.copy()
        p_state['player_mana'] -= 173
        p_state['mana_spent'] += 173
        p_state['poison_timer'] = 6
        new_states.append(p_state)
    if state['player_mana'] >= 229 and not state['recharge_timer']:
        r_state = state.copy()
        r_state['player_mana'] -= 229
        r_state['mana_spent'] += 229
        r_state['recharge_timer'] = 5
        new_states.append(r_state)

    for new_state in new_states:
        # only proceed with effects and boss's turn if player's turn didn't end the battle
        if new_state['boss_hp'] > 0:
            apply_effect(new_state)
            if new_state['boss_hp'] > 0:
                # boss's turn
                new_state['player_hp'] -= max(1, boss_dmg - new_state['player_armor'])

    return new_states

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

def solve(player_stats, boss_stats):
    """
    Given the path of a file containing valid input, return the solution
    """
    # NOTE: remember that effect spells can't be cast if their timers are still active (nonzero)
    best_found = 0
    initial = {'player_hp': player_stats[0], 'player_armor': 0, 'player_mana': player_stats[1],
               'boss_hp': boss_stats[0], 'shield_timer': 0, 'poison_timer': 0, 'recharge_timer': 0,
               'mana_spent': 0}
    fringe = [initial]
    while fringe:
        # need DFS instead of BFS to find an initial solution to defeating the boss and provide a reference for mana spend
        state = fringe.pop()
        if best_found and state['mana_spent'] > best_found or state['player_hp'] <= 0 or state['player_mana'] < 0:
            continue
        if state['boss_hp'] <= 0:
            if (not best_found or state['mana_spent'] < best_found):
                best_found = state['mana_spent']
            continue
        fringe.extend(run_turns(state, boss_stats[1]))

    return best_found

# ----
# main
# ----

if __name__ == "__main__":
    sample_player = (10, 250)
    sample_boss = (13, 8)
    print(solve(sample_player, sample_boss))
    sample_boss = (14, 8)
    print(solve(sample_player, sample_boss))
    player = (50, 500)
    print(solve(player, parse('input')))
