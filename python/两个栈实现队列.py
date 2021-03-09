class CQueue:

    def __init__(self):
    	self.left_stack = []
    	self.right_stack = []


    def appendTail(self, value):
    	for i in range(len(self.right_stack)):
    		self.left_stack.append(self.right_stack.pop())

    	self.append(value)


    def deleteHead(self):
    	if(len(self.right_stack) != 0):
    		return self.right_stack.pop()
    	for i in range(len(self.left_stack)):
    		self.right_stack.append(self.left_stack.pop())
    	return self.right_stack.pop()                  

a = [1, 2, 3]
b = a.pop()
print(b)