"""
Given containers of certain sizes, find how many combinations exactly fit 150 liters
"""

from itertools import combinations, chain

# -----
# solve
# -----

def solve(filepath, goal):
    """
    Given the path of a file containing valid input, return the solution
    """
    with open(filepath, encoding='utf-8') as file:
        containers = list(map(int, file))

    containers.sort(reverse=True)
    start = start_sum = 0
    # note: in this while loop, start_sum lags behind start. but we want start to be ind + 1
    while start_sum < goal:
        start_sum += containers[start]
        start += 1

    containers.reverse()
    end = len(containers)
    end_sum = sum(containers)
    while end_sum > goal:
        end -= 1
        end_sum -= containers[end]

    return len([combo for combo in chain.from_iterable(combinations(containers, i) for i in range(start, end + 1)) if sum(combo) == goal])

# ----
# main
# ----

if __name__ == "__main__":
    print(solve('input', 150))
