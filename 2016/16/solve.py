"""
Given some initial data, generate more pseudo-random data to fill the disk and find the checksum
"""

def generate_checksum(data):
    """
    Find the checksum of the given data
    """
    chksum = data
    while not len(chksum) % 2:
        chksum = ''.join('1' if chksum[i] == chksum[i + 1] else '0' for i in range(0, len(chksum), 2))
    return chksum

def generate_data(initial, disk_len):
    """
    Generate pseudo-random data to expand the initial data to the disk size
    """
    data = initial
    while len(data) < disk_len:
        b = ''.join('1' if c == '0' else '0' for c in reversed(data))
        data += '0' + b
    return data[:disk_len]

def solve(data, disk_len):
    """
    Given input to the problem, return the solution
    """
    return generate_checksum(generate_data(data, disk_len))

if __name__ == '__main__':
    print(f'111100001010 should expand to\n1111000010100101011110000\ngot\n \
          {generate_data('111100001010', len('1111000010100101011110000'))}')
    print(solve('01000100010010111', 272))
    # there must be some way to more cleverly work out this solution without generating a 35 million
    # character string, but I don't know what it is
    print(solve('01000100010010111', 35651584))
