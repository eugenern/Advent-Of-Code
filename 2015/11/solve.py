"""
Given santa's current password, find the next password that meets the new requirements
"""

from itertools import combinations

# ------------------------------------------
# does pass have seq of 3 increasing letters
# ------------------------------------------

def three_consec_increasing(pw):
    """
    Given a password, return whether it contains 3 consecutive increasing letters (no wrap-around)
    """
    return any(ord(c) + 2 == ord(pw[i + 1]) + 1 == ord(pw[i + 2]) for i, c in enumerate(pw[:-2]))

# ---------------------------------
# does pass have only valid letters
# ---------------------------------

def only_valid_letters(pw):
    """
    Given a password, return whether it doesn't contain i, o, or l
    """
    return all(char not in pw for char in ('i', 'o', 'l'))

# ---------------------------------------------
# does pass have two different pairs of letters
# ---------------------------------------------

def two_diff_pairs(pw):
    """
    Given a password, return whether it contains two different and non-overlapping pairs of letters
    """
    pair_beginnings = []
    for i, c in enumerate(pw[:-1]):
        if c == pw[i + 1]:
            pair_beginnings.append(i)

    return len(pair_beginnings) > 1 and \
           any(abs(i1 - i2) > 1 and pw[i1] != pw[i2] for i1, i2 in combinations(pair_beginnings, 2))

# -------------------------
# iterate password sequence
# -------------------------

def iterate(pw):
    """
    Given a password, return the next password by iterating letters starting from the right
    """
    codes = list(map(ord, pw))
    carry_over = True
    cur_ind = len(codes) - 1
    while carry_over:
        if chr(codes[cur_ind]) == 'z':
            codes[cur_ind] = ord('a')
            cur_ind -= 1
            carry_over = cur_ind >= 0
        else:
            codes[cur_ind] += 1
            carry_over = False
    return ''.join(map(chr, codes))

# -------------
# is pass valid
# -------------

def is_valid(pw):
    """
    Given a password, return whether it complies with the Security-Elf's regulations
    """
    return three_consec_increasing(pw) and only_valid_letters(pw) and two_diff_pairs(pw)

# ------------------
# find next password
# ------------------

def find_next_pass(cur_pass):
    """
    Given a password, iterate until the next accepted password is found
    """
    new_pass = iterate(cur_pass)
    while not is_valid(new_pass):
        new_pass = iterate(new_pass)

    return new_pass

# ----
# main
# ----

if __name__ == "__main__":
    print('testing iterate:')
    print(f'\tzzzzzzzz -> {iterate('zzzzzzzz')}')
    print('testing overall:')
    print(f'\tabcdfezz -> {find_next_pass('abcdfezz')}, expected abcdffaa')
    print(f'\tabcdefgh -> {find_next_pass('abcdefgh')}, expected abcdffaa')
    print(f'\tghijklmn -> {find_next_pass('ghijklmn')}, expected ghjaabcc')
    new_pass = find_next_pass('cqjxjnds')
    print(new_pass)
    print(find_next_pass(new_pass))
