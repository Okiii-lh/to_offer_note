# encoding=utf-8
# 给定升序排列的有序数组，找到两个数使得相加之和等于目标数
# 
def twoSum(nums, target):
	left = 0
	right = len(nums)-1

	while left < right:
		sum_num = nums[left] + nums[right]
		if sum_num == target:
			return [left+1, right+1]
		elif sum_num > target:
			right -= 1
		elif sum_num < target:
			left += 1

	return None