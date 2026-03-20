def minNumberOperations(target) :
    

    dp=[0]*len(target)

    dp[0]=target[0]

    for i in range(1,len(target)):
        if target[i]>target[i-1]:
            dp[i]=dp[i-1]+(target[i]-target[i-1])
        else:
            dp[i]=dp[i-1]
    return dp[len(target)-1]
target=[1,2,3,2,1]
print(minNumberOperations(target))