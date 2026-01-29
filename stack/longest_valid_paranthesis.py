
def longestValidParentheses(s):
    ct=0
    mx=0
    stack=[-1]

    for i in range(len(s)):
        if s[i]=='(':
            stack .append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                mx=max(mx,i-stack[-1])
    return mx
                
s=")()())"
print(longestValidParentheses(s))