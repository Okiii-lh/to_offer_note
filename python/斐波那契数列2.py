# encoding=utf-8
# 
def fib(N):
	if N < 0 :
		return 0
	if N == 1 or N == 2:
		return 1

	res = []
	res[1] = res[2] = 1

	for i in range(3, N+1):
		res[i] = res[i-1] + res[i-2]

	return res[N]


fib(5)