# encoding=utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 反转整个链表 双指针
def reverse_double_pointer(head):
	curr = head
	pos = curr.next
	reverse_head = head

	while(pos):
		reverse_head.next = None
		curr.next = reverse_head
		curr = pos
		pos = pos.next

	return reverse_head



# 反转整个链表 递归
def reverse_recursion(head):

	if head.next is None:
		return head

	ret = reverse_recursion(head.next)
	head.next.next = head
	head.next = None

	return ret

successor = None

# 反转链表的前n个元素
def reverseN(head, n):
	if n == 1:
		successor = head.next

		return head

	ret = reverseN(head.next, n-1)
	head.next.next = head
	head.next = successor

	return ret



# 反转链表的一部分
def reverse_part(head, start, end):
	if start == 1:
		reverseN(head, end)

	head.next = reverse_part(head.next, start-1, end-1)

	return head