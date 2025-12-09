"""
Given a list of IP addresses, determine how many of them support Transport Layer Snooping
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
    given iterators over the hypernet sequences and over the other parts,
    determine whether ABBAs are placed appropriately
    """
    return check_hypernets(iters[0]) and check_others(iters[1])

# ---------------
# check_hypernets
# ---------------

def check_hypernets(seq_iter):
    """
    given iterator over the hypernet sequences, check that there are no ABBAs
    """
    return not any(map(has_abba, seq_iter))

# ------------
# check_others
# ------------

def check_others(seq_iter):
    """
    given iterator over the other parts, check that there is at least one ABBA
    """
    return any(map(has_abba, seq_iter))

# --------
# has_abba
# --------

def has_abba(match_obj):
    """
    given a match object, determine whether the matched sequence contains an ABBA
    """
    seq = match_obj.group()
    return any(map(lambda x: seq[x] != seq[x + 1] and seq[x : x + 2] == seq[x + 3 : x + 1 : -1],
                   range(len(seq) - 3)))

# ----
# read
# ----

def read(string):
    """
    get iterators for the hypernet sequences and the supernet sequences from the IP address
    """
    # note: supernet pattern assumes that there exists at least one hypernet
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
