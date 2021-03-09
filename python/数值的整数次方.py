# coding=utf-8

def power(base, exponent):
	"""
	手动实现power函数
	需要考虑的边界值
	当指数为负数的情况
	当底数为0的情况
	"""
	result = 1.0
	# 当底数为0切指数为负数时，即0做除数
	if base == 0 and exponent < 1:
		return 0

	# 当指数为0时 直接返回为1
	if exponent == 0:
		return 1

	if exponent < 0:
		abs_exponent = - exponent
	else:
		abs_exponent = exponent

	for i in range(abs_exponent):
		result *= base

	if exponent < 0:
		result = 1.0/result

	return result


result = power(2, -1)	

print(result)


def power2(base, exponent):
	if exponent == 0:
		return 1
	if exponent == 1:
		return base

	result = power2(base, exponent>>1)
	result *= result

	if exponent & 0X1 == 1:
		result *= base

	return result

result2 = power2(2, 4)
print(result2)