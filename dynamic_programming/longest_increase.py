
def longestIncreasingPath( matrix):
    m=len(matrix)
    n=len(matrix[0])

    moves=[(0,1),(1,0),(-1,0),(0,-1)]

    dp=[[0]*n for _ in range(m)]

    def dfs(x,y):

        if dp[x][y]!=0:
            return dp[x][y]
        mx=1
        for a,b in moves:
            nx=x+a
            ny=y+b

            if 0 <= nx < m and 0 <= ny < n:
                if matrix[nx][ny] > matrix[x][y]:
                    l = 1 + dfs(nx, ny)
                    mx = max(mx, l)
        dp[x][y]=mx
        return mx
    ans=0
    for i in range(m):
        for j in range(n):
            ans=max(ans,dfs(i,j))
    return ans


matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))