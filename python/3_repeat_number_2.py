# encoding=utf-8

# 不修改数组，查找重复元素
test_data = [2, 3, 5, 4, 3, 2, 6, 7]


def getDuplicated(nums, len):

	if nums is None or len <=0:
		return -1

	end = len - 1
	start = 1

	while(end > start):
		middle = (start + end) / 2
		count = getCount(nums, middle, start)
		if(count > (middle - start) + 1):
			end = middle
		else:
			start = middle + 1

		# 如果相等，说明找到了，返回找到的值
		if(start == end):
			if count > 1:
				return start
			else:
				break


def getCount(nums, middle, start):
	if nums is None:
		return 0

	count = 0
	for num in nums:
		if num >= start and num <= middle:
			count += 1

	return count


num = getDuplicated(test_data, 8)
print(num)