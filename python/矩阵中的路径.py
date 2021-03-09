# coding=utf-8

def findRoad(matrix, rows, cols, path):
	if not matrix or rows < 0 or cols < 0 or path is None:
		return False

	boolmaxtrix = [0] * (rows * cols)

	pathLength = 0

	for rows in range(rows):
		for col in range(col):
			if hasPathCore(matrix, rows, cols, row, col, path, pathLength, boolmaxtrix):
				return True

		return False



def hasPathCore(matrix, rows, cols, row, col, path, pathLength, boolmaxtrix):
	if len(path) == pathLength:
		return True

	hasNextPath = False

	if row > 0 and row < rows and col > 0 and col < cols and
		matrix[rows*cols + col] == path[pathLength] and not 
		boolmaxtrix[row*cols + col]:

		pathLength += 1
		boolmaxtrix[row * cols + col] = True

		hasNextPath = (hasPathCore(matrix, rows, cols, row-1, col, path, pathLength, boolmaxtrix)
						or hasPathCore(matrix, rows, cols, row, col+1, path, pathLength, boolmaxtrix)
						or hasPathCore(matrix, rows, cols, row+1, col, path, pathLength, boolmaxtrix)
						or hasPathCore(matrix, rows, cols, row, col-1, path, pathLength, boolmaxtrix))

		if not hasNextPath:
			pathLength -= 1
			boolmaxtrix[rows*cols + col] = False

	return hasNextPath




