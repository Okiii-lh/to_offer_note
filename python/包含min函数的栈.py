# encoding=utf-8
# 定义一个栈的数据结构，并实现一个能够得到栈的最小元素的min函数
# 该栈中，调用min、push、pop时间复杂度都为O(1)

class MinStack:
	def __init__(self):
		self.A, self.B = [], []

	def push(self, x):
		self.A.append(x)
		if self.B is None or self.B[-1] > x:
			self.B.append(x)

	def pop(self):
		if self.A.pop() == self.B[-1]:
			self.B.pop()

	def top(self):
		return self.A[-1]

	def min(self):
		return self.B[-1]