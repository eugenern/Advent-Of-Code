"""
Given a salt for one-time pad keys, find the index of the 64th key
"""

from hashlib import md5

def stretch_hash(salt, i):
    """
    Given a salt and an index, run md5 hash 2017 times
    """
    m = md5((salt + str(i)).encode()).hexdigest()
    for _ in range(2016):
        m = md5(m.encode()).hexdigest()
    return m

def solve(salt):
    """
    Append indices to salt until the 64th key is found
    """
    confirmed_keys = []
    potential_keys = []
    i = 0
    # NOTE: had to handle an issue where later indices can get confirmed before earlier indices
    # e.g. ind 39 gets confirmed at ind 816 while ind 92 gets confirmed at ind 200
    # fix is to go 1000 beyond 64th confirmation to look for more confirmations for earlier indices
    while len(confirmed_keys) < 64 or i < 1000 + sorted(confirmed_keys)[63]:
        m = stretch_hash(salt, i)
        # find first triple
        for m_i in range(len(m) - 2):
            if m[m_i] == m[m_i + 1] == m[m_i + 2]:
                potential_keys.append((i, m[m_i]))
                break
        # check potential keys
        while potential_keys and i - potential_keys[0][0] > 1000:
            del potential_keys[0]
        confirm = []
        for pk_i, key in enumerate(potential_keys[:-1]):
            if key[1] * 5 in m:
                confirmed_keys.append(key[0])
                # print(f'ind {key[0]} is a key because {key[1]} appears 5x in hash for ind {i}')
                confirm.append(pk_i)
        confirm.reverse()
        for pk_i in confirm:
            del potential_keys[pk_i]
        i += 1

    return sorted(confirmed_keys)[63]

if __name__ == '__main__':
    print(solve('abc'))
    print(solve('qzyelonm'))
