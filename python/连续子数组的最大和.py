# encoding=utf-8

def maxSubArry(nums):
	for i in range(len(nums)):
		nums[i] += max(nums[i-1], 0)

	return max(nums)