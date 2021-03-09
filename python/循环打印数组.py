# coding=utf-8
# 循环打印二维数组



def print_matrix_clockwisely(numbers, columns, rows):
	"""
	循环打印数组
	循环条件 行数大于起始坐标*2 列数大于起始坐标*2
	"""
	if numbers is None or columns is None or rows is None:
		return 

	start = 0

	while(columns > start*2 and rows > start *2):
		print_matrix(numbers, columns, rows, start)
		start += 1


def print_matrix(numbers, columns, rows, start):
	"""
	打印函数
	"""
	end_X = columns - 1 - start
	end_Y = rows - 1 - start

	for i in range(end_X+1):
		print(numbers[start][i])

	if end_Y > start:
		for i in range(start+1, end_Y+1):
			print(numbers[i][end_X])

	if end_Y > start and end_X > start:
		for i in range(end_X-1, start-1, -1):
			print(numbers[end_Y][i])

	if end_X > start and end_Y > (start+1):
		for i in range(end_Y-1, start+1, -1):
			print(numbers[i][start])

test_num = [[1], [2], [3]]

print_matrix_clockwisely(test_num, 1, 3)

	
