# encoding=utf-8
# 
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_to_double_list(root):
	def dfs(cur):
		if not cur: return None
		dfs(cur.left)

		if pre:
			pre.right, cur.left = cur, pre
		else:
			head = pre
		pre = cur

		dfs(cur.right)

	if not root: return None
	pre = None
	dfs(root)
	head.left, pre.right = pre, head
	return head