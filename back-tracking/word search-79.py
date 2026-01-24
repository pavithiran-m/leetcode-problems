def exist(board, word):
        
        m=len(board)
        n=len(board[0])

        def backtrack(x,y,ind):
            if ind==len(word):
                return True

            if x<0 or y< 0 or x>=m or y>=n or board[x][y]!=word[ind]:
                return False
            t=board[x][y]
            board[x][y]='-'

            if backtrack(x+1,y,ind+1):
                return True
            if backtrack(x-1,y,ind+1):
                return True
            if backtrack(x,y+1,ind+1):
                return True
            if backtrack(x,y-1,ind+1):
                return True
            board[x][y]=t
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if backtrack(i,j,0):
                        return True
        return False