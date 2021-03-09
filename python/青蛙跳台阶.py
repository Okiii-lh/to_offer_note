# coding=utf-8

# 	青蛙跳台阶

def jump(n):
	"""
	递归方式
	"""
	if n == 1:
		return 1
	if n == 2:
		return 2

	return jump(n-1) + jump(n-2)


def jump2(n):
	"""
	循环方式
	"""
	resulto = 0
	result = [1, 2]
	if n <= 2:
		return result[n-1]

	one = 1
	two = 2

	for i in range(2, n):
		resulto = one + two

		one = two
		two = resulto

	return resulto


print(jump(5))
print(jump(5))