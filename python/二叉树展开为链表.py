# encoding=utf-8
# 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root):
	if root is None:
		return None

	flatten(root.left)
	flatten(root.right)

	left = root.left
	right = root.right

	root.left = None
	root.right = left

	p = root
	while not p:
		p = p.right

	p.right = right
