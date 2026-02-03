def knapsack(weight,value,c):
    n=len(weight)
    dp=[[0]*(c+1) for _ in range(n+1)]
    
    
    for i in range(1,n+1):
        for j in range(c+1):
            if weight[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i-1]] +value[i-1],)
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][c],dp

weight=[1,2,3]
value=[10,15,40]
c=4
print(knapsack(weight,value,c))
