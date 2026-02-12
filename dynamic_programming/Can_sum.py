arr=[7,12]
target=210
dp=[False]*(target+1)
dp[0]=True
for i in range(target+1):
    if dp[i]:
        for n in arr:
            if i+n<=target:
                dp[i+n]=True
print(dp[target])

arr = [20, 30, 12]
target = 60

dp = [[] for _ in range(target + 1)]
dp[0] = [[]]   

for i in range(target + 1):
    for c in dp[i]:
        for n in arr:
            if i + n <= target:
                dp[i + n].append(c + [n])

print(dp[target])

