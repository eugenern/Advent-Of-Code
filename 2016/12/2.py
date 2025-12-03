"""
Given some assembunny code, determine what the value in register a will be after the code finishes execution
"""

#!/usr/bin/env python3

# -------
# imports
# -------

import sys

# ----------------
# registers and pc
# ----------------

pc = 0
regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

# ----
# copy
# ----

def copy(val, reg):
	"""
	given either an int or a reg and a reg, copy the val of the first arg to the second arg
	"""
	regs[reg] = int(val) if val < 'a' else regs[val] # super hacky I know

# ---
# inc
# ---

def inc(reg):
	"""
	given a reg, increment the value in that reg
	"""
	regs[reg] += 1

# ---
# dec
# ---

def dec(reg):
	"""
	given a reg, decrement the value in that reg
	"""
	regs[reg] -= 1

# ---
# jnz
# ---

def jnz(val, offset):
	"""
	given either an int or a reg and a offset, if the value of the first arg is not zero, change pc by offset
	"""
	global pc
	if (int(val) if val < 'a' else regs[val]) != 0: # same hack as in copy()
		pc += int(offset) - 1 # hacky way to account for pc incrementing every time the loop iterates

# -----
# solve
# -----

def solve(reader, writer):
	"""
	reader a reader
	writer a writer
	"""
	global pc
	code = list(reader)
	while pc < len(code):
		line = code[pc].split()
		instr = line[0]
		if instr == 'cpy':
			copy(line[1], line[2])
		elif instr == 'inc':
			inc(line[1])
		elif instr == 'dec':
			dec(line[1])
		elif instr == 'jnz':
			jnz(line[1], line[2])

		pc += 1

	writer.write(str(regs['a']))

# ----
# main
# ----

if __name__ == "__main__":
	solve(sys.stdin, sys.stdout)
