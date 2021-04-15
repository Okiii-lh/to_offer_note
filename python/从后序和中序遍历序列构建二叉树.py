# encoding=utf-8
# 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder, postorder):
	if postorder is None:
		return None

	root_val = postorder[-1]

	root = TreeNode(root_val)

	root_mid_idx = inorder.index(root_val)
	root.left = buildTree(inorder[:root_mid_idx], postorder[:root_mid_idx])
	root.right = buildTree(inorder[root_mid_idx+1:], postorder[:root_mid_idx+1:])

	return root
