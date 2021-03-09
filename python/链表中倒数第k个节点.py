class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def findKthNode(pListHead, k):
	if pListHead is None or k == 0:
		return

	tmpNode = pListHead
	resultNode = pListHead

	for i in range(k):
		if tmpNode.next is not None:
			tmpNode = tmpNode.next
		else:
			return

	while tmpNode.next is not None:
		tmpNode = tmpNode.next
		resultNode = resultNode.next

	return resultNode