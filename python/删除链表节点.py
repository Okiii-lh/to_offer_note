# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#         

def deleteNode(head_Node, p_to_deleted):
	"""
	O(10)时间内删除要删除的节点
	"""
	if(head_Node is None or p_to_deleted is None):
		return 

	if p_to_deleted.next is None:
		tmp_node = None
		while(head_Node.next):
			tmp_node = head_Node
			head_nNode = head_Node.next
		tmp_node.next = None
		return 

	if head_Node.next == p_to_deleted:                                                  
		head_Node.next = None
		return

	tmp_node = p_to_deleted.next
	p_to_deleted.val = tmp_node.val
	p_to_deleted.next = tmp_node.next
	tmp_node.next = None

	return 
