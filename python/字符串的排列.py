# encoding=utf-8
# 

def permutation(str):
	if str is None: return

	x = 0
	c = list(str)
	res = []

	def dfs(x):
		if x == len(c)-1:
			res.append(''.join(c))
			return
		dic = set()

		for i in range(x, len(c)):
			if c[i] in dic: continue
			dic.add(c[i])
			c[x], c[i] = c[i], c[x]
			res.append(c)
			dfs(x+1)
			c[i], c[x] = c[x], c[i]

	dfs(x)
	return res