# coding=utf-8
# 两个排序数组A1、A2，A1末尾有足够的空余空间，实验一个函数，把A2中所有数字插入A1中，并且所有数字是排序的
A1 = [1, 3, 3, 5, 9]
A2 = [2, 3, 4, 8, 10]	

def join(A1, A2):
	len_1 = len(A1)
	len_2 = len(A2)

	# 长度注意
	result = [0 for _ in range(0, (len_1+len_2-1))]

	i = len_1 - 1
	j = len_2 - 1
	# 索引数注意
	k = len_1 + len_2 - 2

	while(i != 0 or j != 0):
		if(A2[j] > A1[i]):
			result[k] = A2[j]
			j -= 1
			k -= 1
		elif(A2[j] == A1[i]):
			result[k] = A1[i]
			result[k-1] = A2[j]
			j -= 1
			i -= 1
			k -= 2
		else:
			result[k] = A1[i]
			i -= 1
			k -= 1

	return result


print(join(A1, A2))