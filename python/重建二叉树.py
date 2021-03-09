
pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def construct(pre_order, mid_order):
	if(pre_order is None or mid_order is None):
		return None

	root_val = pre_order[0]
	
	root = TreeNode(root_val)

	root_index = mid_order.index(root)
	
	root.left = construct(pre_order[1	:root_index+1], mid_order[:root_index])
	root.right = construct(pre_order[root_index+1:], mid_order[root_index+1:])

	return root


index = pre_order.index(4)
print(index)

