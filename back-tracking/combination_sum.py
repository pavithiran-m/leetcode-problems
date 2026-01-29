def combinationSum(candidates,target):
    res=[]
    def sub(i,cur,s):
        if s==target:
            res.append(cur[:])
            return
            
        if i>=len(candidates) or s>target:
            return 
        cur.append(candidates[i])

        sub(i,cur,s+candidates[i])
        cur.pop()
        sub(i+1,cur,s)
    sub(0,[],0)
    return res
candidates=[2,3,6,7]
target=7
print(combinationSum(candidates,target))