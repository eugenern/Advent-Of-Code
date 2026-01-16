"""
Given a system of elves delivering presents to houses,
find the first house that receives a certain amount of presents
"""

from math import sqrt

# -----
# solve
# -----

def solve(goal):
    """
    Given the number of presents for a house to receive, return the house number that receives it
    """
    house = 1
    while house * 11 < goal:
        presents = 0
        for elf in range(1, int(sqrt(house)) + 1):
            if not house % elf:
                if house // elf <= 50:
                    presents += elf * 11
                if elf <= 50:
                    presents += house // elf * 11
                if presents >= goal:
                    return house
        house += 1

    return house

# ----
# main
# ----

if __name__ == "__main__":
    print(solve(150))
    print(solve(29000000))
