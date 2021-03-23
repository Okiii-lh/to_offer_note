# encoding = utf-8

def  minNumber(nums):
	def quick_sort(l, r):
		if l >= r:
			return
		i = l
		j = r
		pivot = strs[l]
		while i < j:
			while i < j and strs[j] + strs[l] > strs[l] + strs[j]:
				j -= 1
			strs[i] = strs[j]
			while i < j and strs[i] + strs[l] < strs[l] +strs[i]:
				i += 1
			strs[j] = strs[i]
		strs[i], strs[l] = strs[l], strs[i]
		quick_sort(l, i-1)
		quick_sort(i+1, r)
	
	strs = [str(num) for num in nums]
	quick_sort(0, len(strs)-1)

	return ''.join(strs) 
		
