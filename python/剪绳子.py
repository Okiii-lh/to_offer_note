# coding=utf-8

# 动态规划
def maxProductAfterCutting_dyna(length):
	"""
	动态规划 自底向上
	"""
	if length < 2:
		return 0
	if length == 2:
		return 1
	if length == 3:
		return 2 

	products = [0 for i in range(length+1)]
	products[0] = 0
	products[1] = 1
	products[2] = 2
	products[3] = 3

	max = 0

	for i in range(4, length+1):
		max = 0
		for j in range(1, i/2+1):
			p = products[j] * products[i-j]
			if max < p:
				max = p

			products[i] = max

	max = products[length]

	return max



# 贪心算法
def maxProductAfterCutting_gre(length):
	"""
	贪心算法 每次都选最优
	"""
	if length < 2:
		return 0
	if length == 2:
		return 1
	if length == 3:
		return 2
	
	count_3 = length // 3

	if length % 3 == 1:
		count_3 -= 1

	count_2 = (length - (count_3) * 2) // 2

	return (3 ** count_3) * (2 ** count_2)

result1 = maxProductAfterCutting_dyna(5)
result2 = maxProductAfterCutting_gre(5)

print(result1)
print(result2)