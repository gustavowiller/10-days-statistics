# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from collections import Counter


N = int(raw_input())
X = raw_input()
W = raw_input()

X = map(float, X.split())
W = map(float, W.split())


sum_xw = 0
for i in range(0,N):
	sum_xw = (X[i] + W[i])

result = sum_xw/sum(W)
print("%.1f" % result)
