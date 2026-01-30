def long_1d(s1, s2):
    n, m = len(s1), len(s2)
    dp = [0] * (m + 1)

    mx = 0
    end = 0

    for i in range(1, n + 1):
        for j in range(m, 0, -1):   
            if s1[i - 1] == s2[j - 1]:
                dp[j] = dp[j - 1] + 1
                if dp[j] > mx:
                    mx = dp[j]
                    end = i
            else:
                dp[j] = 0

    return s1[end - mx:end],len(s1[end - mx:end])

s1 = "abcdef"
s2 = "zabcemf"
print(long_1d(s1, s2))
