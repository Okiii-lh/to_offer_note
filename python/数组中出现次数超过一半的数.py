# encoding=utf-8
# 

def majorityElement(nums):
    votes = 0
    for num in nums:
        if votes == 0: x = num
        votes += 1 if num == x else -1
    return x