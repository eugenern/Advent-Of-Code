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

def check(iters):
    """
    given iterators over the hypernet sequences and over the supernet sequences,
    determine whether any ABA in a supernet seq has a BAB in a hypernet seq
    """
    # gather all ABAs from all match_objs in supernet sequences
    # and then search through hypernets for sequence matching any BAB
    abas = set(aba for seq_abas in check_supernets(iters[1]) for aba in seq_abas)
    babs = set(aba[1] + aba[0] + aba[1] for aba in abas)
    return abas and check_hypernets(iters[0], babs)

# ---------------
# check_supernets
# ---------------

def check_supernets(seq_iter):
    """
    given iterator over the supernet sequences, find the abas of each sequence
    """
    return map(get_abas, seq_iter)

# ---------------
# check_hypernets
# ---------------

def check_hypernets(seq_iter, babs):
    """
    given iterator over the hypernet sequences, check that there is at least one BAB
    """
    # don't know how to avoid calling match.group() multiple times
    # and tbh, the commented code may be more readable than the one-liner
    return any(match.group()[i : i + 3] in babs
               for match in seq_iter for i in range(len(match.group()) - 2))
    # for match in seq_iter:
    #     seq = match.group()
    #     for i in range(len(seq) - 2):
    #         if seq[i : i + 3] in babs:
    #             return True
    # return False

# --------
# get_abas
# --------

def get_abas(match_obj):
    """
    given a sequence, find all abas
    """
    seq = match_obj.group()
    return (seq[i : i + 3] for i in range(len(seq) - 2) if seq[i] == seq[i + 2] != seq[i + 1])

# ----
# read
# ----

def read(string):
    """
    get iterators for the hypernet sequences and the supernet sequences from the IP address
    """
    return (re.finditer(r'(?<=\[)[a-z]+(?=\])', string),
            re.finditer(r'(?<=\])[a-z]+|[a-z]+(?=\[)', string))

# -----
# solve
# -----

def solve(reader, writer):
    """
    reader a reader
    writer a writer
    """
    writer.write(str(len(list(filter(check, map(read, reader))))))

# ----
# main
# ----

if __name__ == "__main__":
    solve(sys.stdin, sys.stdout)
