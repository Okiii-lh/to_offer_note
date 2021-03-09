# coding=utf-8

def match(match_str, pattern):
	"""
	模拟正则表达式匹配
	"""
	if match_str is None or pattern is None:
		return False

	match_str_len = len(match_str)
	pattern_len = len(pattern)

	for i in range(pattern_len):
		for j in range(match_str_len):
			if pattern[i+1] == '*':
				if match_str[j] == pattern[i]:
					j += 1
					print(1)
				else:
					i += 2
					print(2)
			elif pattern[i+1] == '.':
				i += 2
				j += 1
				print(3)
			elif pattern[i] == match_str[j]:
				i += 1
				j += 1
				print(4)
			else:
				print(5)
				return False

	return True


match_str = "aaa"
pattern = "a.a"

print(match(match_str, pattern))