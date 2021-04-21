# encoding=utf-8
# 
import collections

def removeDuplicateLetters(s):
	res = []
	freq = collections.Counter(s)

	for c in s:
		if c not in res:
			while res and res[-1] > c and freq[res[-1]] > 0:
				res.pop()
			res.append(c)
		freq[c] -= 1

	return res


def removeDuplicateLetters(s):
	res = []
	freq = collections.Counter(s)
	seen = set()

	for c in s:
		if c not in seen:
			while res and res[-1] > c and freq[res[-1]] > 0:
				seen.discard(res.pop())
			seen.add(c)
			res.append(c)
		freq[c] -= 1

	return ''.join(res)