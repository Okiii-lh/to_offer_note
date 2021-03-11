# encoding=utf-8
# 
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head):
	def dfs(head):
		if not head: return None
		if head in visited:
			return visited[head]
		copy = Node(head.val, None, None)
		visited[head] = copy
		copy.next = dfs(head.next)
		copy.random = dfs(head.random)
		return copy

	visted = {}
	return dfs(head)

def copy_random_list2(head):
	if not head: return None

	now = head

	while(head):
		new_node = Node(now.val, now.next, None)
		new_node.next = now.next
		now.next = new_node
	now = head

	while(now):
		if now.random:
			now.next.random = now.random
		now = now.next.next

	old_head = head
	new_head = head.next

	while old_head:
		old_head.next = old_head.next.next
		if new_head.next:
			new_head.next = new_head.next.next
		old_head = old_head.next
		new_head = new_head.next

	return new_head