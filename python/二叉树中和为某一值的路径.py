# encoding=utf-8


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pathSum(root, sum):
	res, path = [], []

	def recur(root, tar):
		if not root: return
		path.append(root.val)
		tar -= root.val
		if tar == 0 and not root.left and not root.right:
			res.append(list(path))
		recur(root.left)
		recur(root.right)
		path.pop()


	recur(root, sum)
	return res



def path_sum(root, sum):
	res = []
	path = []

	def recur(root, tar):
		if root is None: return
		path.append(root)
		tar -= root.val

		if tar == 0 and not root.left and not root.right:
			res.append(path)

		recur(root.left, tar)
		recur(root.right, tar)
		path.pop()

	recur(root, sum)
	return res