# encoding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthLargest(root, k):
	order = []
	def inorder(root):
		if not root:
			return None
		inorder(root.left)
		order.append(root.val)
		inorder(root.right)

	res = order[-k]
	return res