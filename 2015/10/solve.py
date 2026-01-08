"""
Given a sequence of digits, generate the look-and-say sequence sever times over
"""

# --------
# generate
# --------

def generate_look_say(seq):
    """
    Given a sequence of digits, generate and return its look-and-say sequence
    """
    look_say = []
    i = 0
    while i < len(seq):
        cur_digit = seq[i]
        cur_len = 0
        while i < len(seq) and seq[i] == cur_digit:
            cur_len += 1
            i += 1
        look_say.extend((str(cur_len), cur_digit))

    return ''.join(look_say)

# ----
# main
# ----

if __name__ == "__main__":
    sample = '1'
    for _ in range(5):
        sample = generate_look_say(sample)
    print(f'expected 312211, got {sample}')

    result = '1321131112'
    for _ in range(40):
        result = generate_look_say(result)
    print(len(result))

    for _ in range(10):
        result = generate_look_say(result)
    print(len(result))
