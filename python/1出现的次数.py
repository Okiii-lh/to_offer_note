# encoding=utf-8

def test():
	a = 10

	for i in range(2):
		b = 0
		a = 5
		try:
			c = 1 / 0
		except Exception as e:
			if 1 == 1:
				a = 4
				break
			elif 2 == 2:
				return None, 1
		c = 10

		return 1, 2




a, b = test()

print(a)