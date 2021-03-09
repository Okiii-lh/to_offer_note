# coding=utf-8
# 反转链表
# 
# 这是个简单题

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
	                                                                                              
	curr_node = head
	pre_node = None
	revearse_head = None

	while(curr_node is not None):
		next_node = curr_node.next
		if next is None:
			revearse_head = curr_node
		curr_node.next = pre_node

		pre_node = curr_node
		curr_node = next_node

	return revearse_head