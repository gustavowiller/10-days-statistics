# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from collections import Counter


N = int(raw_input())
nums = raw_input()

nums = map(float, nums.split())


media = sum(nums)/N 
print("%.1f" % media)


nums.sort()
if N % 2 == 0:
	median = (nums[(N/2-1)] + nums[(N/2)])/2
else:
	media = nums[(N/2-1)]


print("%.1f" % median)



c = Counter(nums)


max_value = max(c.items(), key=lambda x: x[1])[1]

list_max_items = [x for (x,y) in c.items() if y == max_value]
if len(list_max_items) > 1:
	print min(list_max_items)
else:
	print list_max_items[0]





