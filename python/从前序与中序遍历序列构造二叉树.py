# encoding=utf-8


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
	if len(preorder) == 0:
		return None

	root = TreeNode(preorder)

	mid = inorder.index(preorder[0])

	root.left = buildTree(preorder[1:mid+1], inorder[:mid])
	root.right = buildTree(preorder[mid+1:], inorder[mid+1:])

	return root