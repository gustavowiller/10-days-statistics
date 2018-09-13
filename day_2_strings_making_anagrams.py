#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter
import string

# Complete the makeAnagram function below.
def makeAnagram(a, b):
	a = Counter(a)
	b = Counter(b)
	
	qtd_move = []	
	for l in string.ascii_lowercase:
		diff = abs(a[l] - b[l])		
		qtd_move.append(diff)
	
	return sum(qtd_move)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

