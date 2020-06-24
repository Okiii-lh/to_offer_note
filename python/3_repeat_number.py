# 数组中重复的数字
# 给定一个数组，数组中一些元素是重复的，找出数组中任意一个重复的数字
# 直接判断是否有重复数字

# hash表法
def repeat_number(numbers, length):
	hash_numbers = [0 for i in range(length)]

	if length <= 0:
		return True

	for number in numbers:
		if number < 0 or number > length-1:
			return  True

	for number in numbers:
		hash_numbers[number-1] += 1

	for number in hash_numbers:
		if number > 1:
			return True


	return False;


# 交换方法 扫描数组 将m与第i个元素比较
def repeat_number2(numbers, length):

	if length <= 0:
		return True

	for number in numbers:
		if number <0 or number > length-1:
			return True

	for i in range(length):
		if numbers[i] != i:
			if numbers[i] == numbers[numbers[i]]:
				return True
			tmp = numbers[i]
			numbers[i] = numbers[tmp]
			numbers[tmp] = tmp

	return False


test_data = [1, 1, 3, 2]

a = repeat_number2(test_data, 4)

print(a)