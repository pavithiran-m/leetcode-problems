nums = [23,78,44,20,19,55,32]
n = len(nums)
        
if n == 1:
    print( nums[0])
else:

    dp = [0] * (n + 1)

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    print(dp[n-1])