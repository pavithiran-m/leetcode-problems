n=10

dp=[0]*(n)

dp[0]=0
dp[1]=1


for i in range(1,n):
    dp[i]=dp[i-1]+dp[i-2]
print(dp)
