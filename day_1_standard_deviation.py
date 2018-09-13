# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

N = int(raw_input())
X = raw_input()

X = map(float,X.split())

media = sum(X)/N

sum_x = 0
for x in X:
	sum_x = math.pow((x - media),2) + sum_x

result = math.sqrt(sum_x / N) 

print("%.1f" % result)

