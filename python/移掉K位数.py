# encoding=utf-8
# 
def removeKDigit(num, k):
	stack = []
	n = len(num) - k
	for digit in num:
		while k and stack and stack[-1] > digit:
			stack.pop()
			k -= 1
		stack.append(digit)

	return ''.join(stack[:n]).lstrip('0') or '0'