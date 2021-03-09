# coding=utf-8
# 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeList(head1, head2):
	if head1 is None:
		return head2
	elif head2 is None:
		return head1

	p_merged_head = None

	if(head1.val < head2.val):
		p_merged_head = head1
		p_merged_head.next = mergeList(head1.next, head2)
	elif(head2.val < head1.val):
		p_merged_head = head2
		p_merged_head.next = mergeList(head1, head2.next)

	return p_merged_head