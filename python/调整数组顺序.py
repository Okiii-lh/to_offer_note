# coding=utf-8

def reorder_1(nums):
	"""
	解法一
	双指针法
	"""
	if nums is None:
		return 

	begin = 0
	end = len(nums)-1

	while begin < end:
		if(nums[begin] % 2 == 0):
			if(nums[end] % 2 != 0):
				tmp = nums[begin]
				nums[begin] = nums[end]
				nums[end] = tmp
				begin += 1
				end -= 1
			else:
				end -= 1
		else:
			if(nums[end] % 2 != 0):
				begin += 1
			else:
				begin += 1
				end -= 1

	return nums


num = [1, 2, 3, 4, 5]
result = reorder_1(num)
print(num)