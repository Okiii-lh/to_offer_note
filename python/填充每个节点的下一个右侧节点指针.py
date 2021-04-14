# encoding=utf-8

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def connect(root):
	if root is None:
		return root

	connectTwo(root.left, root.right)

	return root


def connectTwo(node1, node2):
	if node1 is None or node2 is None:
		return


	node1.next = node2

	connectTwo(node1.left, node1.right)
	connectTwo(node1.right, node2.left)
	connectTwo(node2.left, node2.right)
