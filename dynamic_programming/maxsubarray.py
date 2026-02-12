def maxsum(arr):
    n=len(arr)
    dp=[0]*n
    dp[0]=arr[0]
    
    for i in range(1,n):
        dp[i]=max(arr[i],dp[i-1]+arr[i])
        
    for i in range(len(arr)):
        print(f"Max subarray sum ending at index {i}: {dp[i]}")
    return max(dp)

arr=[-2,1,-3,4,-1,2,1,-5,4]
print(maxsum(arr))