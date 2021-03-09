# coding=utf-8
# 


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def HasSubTree(root1, root2):

	result = False

	if root1 is not None and root2 is not None:
		if root1.val == root2.val:
			result = DoesTree1HasTree2(root1, root2)
		if not result:
			result = HasSubTree(root1.left, root2)
		if not result:
			result = HasSubTree(root1.right, root2)


def DoesTree1HasTree2(root1, root2):
	
	if root2 is None:
		return True

	if root1 is None:
		return False

	if root1.val != root2.val:
		return False

	return DoesTree1HasTree2(root1.left, root2.left) and DoesTree1HasTree2(root1.right, root2.right)