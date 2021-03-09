# coding=utf-8

def isNum(match_str):
	"""
	判断一个字符串是否表示数字
	"""
	match_str = match_str.strip()

	vdot = vdigit = ve = False

	for i, c in enumerate(match_str):
		if c in ['+', '-']:
			if i > 0 and [match_str[i-1] not in ['E', 'e']]:
				return False
		elif c == '.':
			if vdot or ve:
				return False
			vdot = True
		elif c in ['E', 'e']:
			if ve or (not vdigit):
				return False
			ve = True
			vdigit = False
		elif c.isdigit():
			vdigit = True
		else:
			return False

	return vdigit

