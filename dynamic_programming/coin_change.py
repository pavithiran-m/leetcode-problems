def coinChange(coins,amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0

    for i in range(1,amount+1):
        for c in coins:
            if i-c>=0:
                dp[i]=min(dp[i],dp[i-c]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

coins=[2,3,5]
amount=11
print(coinChange(coins,amount))
