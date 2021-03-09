# encoding=utf-8
# 
# 从上到下打印二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order(root):
	result = []
    if root is not None:

        memory = []
        memory.append(root)
        
        while memory:
            result.append(memory[0].val)
            if memory[0].left:
                memory.append(memory[0].left)

            if memory[0].right:
                memory.append(memory[0].right)

            del memory[0]
        
    return result





