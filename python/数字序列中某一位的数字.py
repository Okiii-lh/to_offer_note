# encoding=utf-8
#

def digitAtIndex(index):
	if index <= 10 :
		return index
	result = 0

	i = 1
	count = index - 10
	while(True):
		if i*(10**(i-1))*9 >= index:
			break
		count = count - (10 ** (i))
		i = i+1

	count = index / i
	mo = index % i

	result = str(count+(10 ** (i)))[mo]

	return result
	


print(digitAtIndex(11))