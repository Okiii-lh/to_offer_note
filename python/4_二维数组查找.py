# coding=utf-8

test_data = [
	[1, 2, 8, 9],
	[2, 4, 9, 12],
	[4, 7, 10, 13],
	[6, 8, 11, 15]
]

def search_in_two_matrix(matrix, target, rows, cols):
	found = False

	if(matrix is None or rows <= 0 or cols <= 0):
		return found

	row = 0
	col = cols - 1

	while(row < rows and col >= 0):
		tmp = matrix[row][col]
		if(tmp == target):
			found = True
			break
		elif(tmp > target):
			col -= 1
		else:
			row += 1

	return found


result = search_in_two_matrix(test_data, 7, 4, 4)
print(result)
