def generate(n):
    
    res=[]

    def backtrack(op,cl,p):

        if op==n and cl==n:
            res.append(p)

            return 

        if op <n:
            backtrack(op+1,cl,p+'(')
        if cl<op:
            backtrack(op,cl+1,p+')')
        
    backtrack(0,0,'')
    return res
n=3
print(generate(n))