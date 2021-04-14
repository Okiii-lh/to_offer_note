# encoding=utf-8
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def constructTree(nums):
	if len(nums) == 0:
		return None

	max_index = 0
	max_value = 0

	for i in len(nums):
		if nums[i] >= max_value:
			max_index = i
			max_value = nums[i]

	root = TreeNode(max_value)
	root.left = constructTree(nums[0:max_index])
	root.right = constructTree(nums[max_index:])

	return root


def constructTree2(nums):
	if nums is None:
		return None

	max_value = max(nums)
	max_index = nums.index(max_value)

	root = TreeNode(max_value)
	root.left = constructTree2(nums[:max_index])
	root.right = constructTree2(nums[max_index:])

	return root