
def combinationSum2(candidates, target):
    candidates.sort()  
    res = []
    n = len(candidates)

    def sub(i, cur, s):
        if s == target:
            res.append(cur[:])
            return
        
        if i >= n or s > target:
            return

        
        cur.append(candidates[i])
        sub(i + 1, cur, s + candidates[i])
        cur.pop()

        
        j = i
        while j + 1 < n and candidates[j] == candidates[j + 1]:
            j += 1

        sub(j + 1, cur, s)

    sub(0, [], 0)
    return 
candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates, target))