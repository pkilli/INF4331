#!/user/bin/env python3

import sys
import os.path
import glob

for pattern in sys.argv[1:]:
	for filename in glob.glob(pattern):  # for reading severeal files when typing *.py
		infile = open(filename,'r')
		nChar = 0
		nWords = 0
		nLines = 0
		lines = infile.readlines()
		for line in lines:
			nLines += 1
			wordsInLine = line.split()
			for i in range(len(wordsInLine)):
				words = wordsInLine[i]
				nWords += 1
				char = [ ch for ch in words]
				for j in range(len(char)):
					nChar += 1
		infile.close()

		print (nLines, nWords, nChar, filename)
		
