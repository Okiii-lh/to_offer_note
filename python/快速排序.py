# endocing=utf-8


def quick_sort(nums):
	if len(nums) < 2:
		return nums

	pivot = nums[0]
	less = [i for i in nums[1:] if i < pivot]
	hight = [i for i in nums[1:] if i > pivot]

	return quick_sort(less) + [pivot] + quick_sort(hight)

def quick_sort2(alist, start, end):

    if start >= end:  
        return
    mid = alist[start]  
    low = start 
    high = end 
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]  
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]  
    alist[low] = mid  
    
    quick_sort2(alist, start, low - 1)  
    quick_sort2(alist, low + 1, end)  


def quick_sort3(nums):
	if len(nums) < 2:
		return nums

	pivot = nums[0]
	left = 0
	right = len(nums) - 1

	while left < right:
		while left < right and nums[right] > pivot:
			right -= 1
		nums[left] = nums[right]
		while left < right and nums[left] < pivot:
			left += 1
		nums[right] = nums[left]

	nums[right] = pivot
	quick_sort3(nums[:left])
	quick_sort3(nums[left+1])
 

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort2(alist, 0, len(alist) - 1)
# result = quick_sort(alist)
print(alist)
