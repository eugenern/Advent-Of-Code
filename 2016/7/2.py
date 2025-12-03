"""
Given a list of IP addresses, determine how many of them support Super Secret Listening
"""

# -------
# imports
# -------

import sys
import re

# -----
# check
# -----

def check(matches):
    """
    given iterators over the hypernet sequences and over the supernet sequences,
    determine whether any ABA in a supernet seq has a BAB in a hypernet seq
    """
    # get ABAs from all match_objs in supernet sequences
    # and check if any ABA has a BAB in the hypernet seqs
    for abas in check_supernet(matches[0]):
        for aba in abas:
            if has_bab(aba, matches[1]):
                return True
    return False

# --------------
# check_supernet
# --------------

def check_supernet(seq_list):
    """
    given list of the supernet sequences, find the abas of each sequence
    """
    return map(get_abas, seq_list)

# -------
# has_bab
# -------

def has_bab(aba, seq_list):
    """
    given aba and list of hypernet sequences, check if a corresponding bab exists
    """
    for seq in seq_list:
        if any(map(
            lambda x: seq[x] == aba[1] == seq[x + 2]
            and seq[x + 1] == aba[0],
            range(len(seq) - 2))):
            return True
    return False

# --------
# get_abas
# --------

def get_abas(seq):
    """
    given a sequence, find all abas
    """
    return map(
        lambda x: seq[x:x+3],
        filter(lambda x: seq[x] != seq[x + 1] and seq[x] == seq[x + 2], range(len(seq) - 2))
        )

# ----
# read
# ----

def read(string):
    """
    get iterators for the hypernet sequences and the supernet sequences from the IP address
    """
    # can use an iterator for one of them? but need the whole list of strings for the other
    return (re.findall(r'(?<=\[)[a-z]+(?=\])', string),
            re.findall(r'(?<=\])[a-z]+|[a-z]+(?=\[)', string))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(str(len([line for line in reader if check(read(line))])))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
