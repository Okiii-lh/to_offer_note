# encoding=utf-8
# 
import collections

def minWindow(s, t):
	need = collections.defaultdict(int)
	for i in t:
		need[t] += 1

	need_cnt = len(t)
	start = 0
	res = (0, 0)

	for i, c in enumerate(s):
		if need[c] > 0:
			need_cnt -= 1
		need[c] -= 1
		if need_cnt == 0:
			while True:
				c = s[start]
				if need[c] == 0:
					break
				else:
					need[c] += 1
					start += 1
			if j - start < res[1] - res[0]:
				res = (start, j)
			need[s[start]] += 1
			need_cnt += 1
			start += 1

	return "" if res[1] > len(s) else s[res[0]:res[1]+1]



def minWindow(s, t):
	need = collections.defaultdict(int)
	for c in t:
		need[c] += 1

	need_cnt = len(t)
	left = 0
	res = (0, float('inf'))

	for right, c in enumerate(s):
		if need[c] > 0:
			need_cnt -= 1
		need[c] -= 1
		if need_cnt == 0:
			while True:
				c = s[left]
				if need[c] == 0:
					break
				else:
					need[c] += 1
					left += 1
			if right - left < res[1] - res[0]:
				res = (left, right)
			need_cnt += 1
			need[s[left]] += 1
			left += 1

	return "" if res[1] > len(s) else s[res[0]:res[1]+1]