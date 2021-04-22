# encoding=utf-8

def coinChange(coins, amount):
	dp = [float('inf')] * (amount+1)
	dp[0] = 0
	for coin in coins:
		for i in range(coin, amount+1):
			dp[i] = min(dp[i], dp[i-coin]+1)

	return dp[amount] if dp[amount] != float('inf') else -1


res = coinChange([1, 3, 5], 5)
print(res)


