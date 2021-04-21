# encoding=utf-8
# 
def lengthOfLongestSubstring(s):
	L = len(s)
	if L < 2:
		return L

	left = 0
	right = 1
	cnt = 1

	while right < L:
		while right < L and s[right] not in s[left:right]:
			right += 1
		cnt = max(cnt, right-left)
		if right != L:
			left += s[left:right].index(s[right])+1

	return cnt