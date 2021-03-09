# coding=utf-8
# 斐波那契数列
def fibonacci(n):
	"""
	递归方式
	"""
	if n == 0:
		return 0
	if n == 1:
		return 1

	return fibonacci(n-1) + fibonacci(n-2)



def fibonacci2(n):
	"""
	非递归
	"""
	result = [0, 1]

	if n < 2:
		return result[n]

	fibN = 0
	fibNOne = 1
	fibNTwo = 1

	for i in range(2, n):
		fibN = fibNOne + fibNTwo

		fibNTwo = fibNOne
		fibNOne = fibN

	return fibN


result = fibonacci2(10)
result2 = fibonacci(10)
print(result)
print(result2)



