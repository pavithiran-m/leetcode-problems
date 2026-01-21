def subset(arr,tar):
    
    curr=[]
    res=[]
    
    # def backtrack(i):
    #     if i==len(arr):
    #         res.append(path[:])
    #         return 
    #     path.append(arr[i])
    #     backtrack(i+1)
    #     path.pop()
    #     backtrack(i+1)
        
    # backtrack(0)
    # return res
    def backtrack(curr,i,s):
        if s==tar:
            res.append(curr[:])
            return 
        if i==len(arr) or s>=tar:
            return 
        curr.append(arr[i])
        backtrack(curr,i+1,s+arr[i])
        curr.pop()
        backtrack(curr,i+1,s)
        
    backtrack(curr,0,0)
    return res
    
nums=[1,2,3,4,5]
tar=8
print(subset(nums,tar))