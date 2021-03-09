# coding=utf-8
# 


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def MirrorTree(root):
	if root is None:
		return 
	if root.left is None and root.right is None:
		return 

	tmpNode = root.left
	root.left = root.right
	root.right = tmpNode

	if root.left:
		MirrorTree(root.left)
	if root.right:
		MirrorTree(root.right)