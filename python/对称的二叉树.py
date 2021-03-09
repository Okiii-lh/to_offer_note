# coding=utf-8
# 


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetrical(root):
	return isS(root, root)


def isS(roo1, root2):
	if roo1 is None and root2 is None:
		return True
	if root1 is None or root2 is None:
		return False

	if root2.val != root1.val:
		return False

	return isS(root1.left, root2.right) and isS(root1.right, root2.left)


