# coding=utf-8
# 
# 栈的压入弹出序列
# 给定两个序列，第一个为栈的压入序列，判断第二个序列是否是栈的弹出序列
# 
# 
# 
def IsPopOrder(pushed, poped):
	"""
	使用辅助栈
	"""
	stack, i =[], 0

	for num in pushed:
		stack.append(num)
		while stack and stack[-1] == poped[i]:
			stack.pop()
			i += 1

	return not stack	
		


