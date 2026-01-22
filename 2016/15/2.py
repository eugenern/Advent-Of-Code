"""
Given a sequence of discs of varying sizes and positionings, find the earliest time at which
dropping a capsule will let it fall through all discs
"""

from math import prod

def mod_mult_inverse(nk, mk):
    """
    Given one of the operands of the mod operation, nk, and the product of the mod operands of all
    the other mod operations, find the modular multiplicative inverse
    """
    a, b = max(nk, mk), min(nk, mk)
    # NOTE: s1, s2, s3 are not actually needed for this function
    steps = [(a, b, a // b, a % b, 1, 0, 1, 0, 1, -(a // b))]
    while a % b:
        a, b = steps[-1][1], steps[-1][3]
        q, r = a // b, a % b
        old_s2, old_s3, old_t2, old_t3 = steps[-1][5], steps[-1][6], steps[-1][8], steps[-1][9]
        steps.append((a, b, q, r, old_s2, old_s3, old_s2 - (q * old_s3), old_t2, old_s3, old_t2 - (q * old_t3)))
    return steps[-1][-2] % nk

def line_up_release(time_to_disc, pos_at_time_0, cycle_len):
    """
    Given the time a capsule takes to reach the disc, the position of the disc at time 0, and
    the total # of positions on the disc, return the first time to drop the capsule such that
    the disc would be at position 0 when the capsule reaches it
    """
    time_when_pos_0 = cycle_len - pos_at_time_0
    return (time_when_pos_0 - time_to_disc) % cycle_len

def parse(line):
    """
    Given a line describing a disc's size and positioning, return the basic characteristics
    """
    tokens = line.split()
    return [int(tokens[3]), int(tokens[-1].rstrip('.'))]

def solve(filepath):
    """
    Given the path to an input file, read the input and find the solution
    """
    with open(filepath, encoding='utf-8') as file:
        discs = list(map(parse, file))
    discs.append([11, 0])

    for i, disc in enumerate(discs):
        disc[1] = line_up_release(i + 1, disc[1], disc[0])

    # the naive approach would work: iterate through multiples of the greatest disc size (disc[0])
    # until a time is found such that t % disc[0] == disc[1] for all discs
    # a more satisfying solution would be to implement the Chinese Remainder Theorem to solve the
    # system of congruences (modular equations)
    # NOTE: in our input, all disc sizes are pairwise coprime, so there exists one unique solution

    n = prod(disc[0] for disc in discs)
    ms = [n // disc[0] for disc in discs]
    inverses = [mod_mult_inverse(disc[0], ms[i]) for i, disc in enumerate(discs)]

    return sum(disc[1] * ms[i] * inverses[i] for i, disc in enumerate(discs)) % n

if __name__ == '__main__':
    print(solve('input'))
