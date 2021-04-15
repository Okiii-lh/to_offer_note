# encoding=utf-8
# 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 判断链表是否有环
def hasCycle(head):
	fast, slow = head

	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next

		if fast == slow:
			return True

	return False


# 链表中含有环，返回环的起始位置
def detectCycle(head):
	fast, slow = head

	while not fast and not fast.next:
		fast = fast.next.next
		slow = slow.next
		if fast == slow:
			break

	slow = head
	while slow != fast:
		slow = slow.next
		fast = fast.next

	return slow


# 链表的中点
def midCycle(head):
	fast, slow = head
	while not (fast and fast.next):
		fast = fast.next.next
		slow = slow.next

	return slow
