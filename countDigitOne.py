def countDigitOne(n):
    ct=0
    f=1

    while f<=n:
        l=n%f
        c=(n//f)%10
        h=n//(f*10)

        if c==0:
            ct+=h*f
        elif c==1:
            ct+=(h*f)+(l+1)

        else:
            ct+=(h+1)*f
        f*=10
    return ct

n=13
print(countDigitOne(n))