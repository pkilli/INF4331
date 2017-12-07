import argparse
from typing import List

def equalize(arr1: List, arr2: List, element=""):
    
    size_orig = len(arr1)
    size_mod = len(arr2)
    if size_orig < size_mod:
        for i in range(size_mod - size_orig):
            arr1 += [element]
    elif size_orig > size_mod:
        for i in range(size_orig - size_mod):
            arr2 += [element]

    return arr1, arr2



def compare(orig_file: str, mod_file: str):
	""" comparing lines of two files, printing and writing to file.
		It should go through the files line by line, and if a line has not been
		modified, print it with a 0 in front, if it has been added, print it with a + in
		front, and if it has been deleted, print it with a - in front. If a line has been
		modified, treat it as being a deletion of the original line, and then an addition
		of the modified line
	"""
	orig_file = orig_file.split("\n")
	mod_file = mod_file.split("\n")

	orig_file, mod_file = equalize(orig_file, mod_file)
	with open("diff_output.txt", 'a') as out:
		for line_o, line_mod in zip(orig_file, mod_file):
			if line_o == line_mod:
				line = "0 " + line_o
				out.write(line + '\n')
				print("0", line_o)
			elif line_o != line_mod and line_mod == '':
				line = "- " + line_o
				out.write(line + '\n')
				print("-", line_o)
			elif line_o == '':
				line = "+ " + line_o
				out.write(line + '\n')
				print("+ ", line_mod)
			elif line_o != line_mod:
				line = "- " + line_o
				line2 = "+ " + line_mod
				out.write(line + '\n')
				out.write(line2 + '\n')
				print("-", line_o)
				print("+", line_mod)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("original")
    parser.add_argument("new")
    args = parser.parse_args()

    with open(args.original) as f, open(args.new) as mod:
        original = f.read()
        new = mod.read()

    compare(original, new)

