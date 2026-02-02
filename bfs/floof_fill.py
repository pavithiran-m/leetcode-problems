from collections import deque
def floodFill(image, sr, sc):
    n=len(image)
    m=len(image[0])
    start=image[sr][sc]
    dirs=[(0,1),(1,0),(0,-1),(-1,0),
          (-1,1),(1,1),(1,-1),(-1,-1)]
    ct=0
    if image[sr][sc]==1:
        return image
    if image[sr][sc]==0:
        image[sr][sc]=2
        ct+=1
    q=deque([(sr,sc)])
    
    while q:
        a,b=q.popleft()
        
        for i,j in dirs:
            nx,ny=a+i,b+j
            if 0<=nx<n and 0<=ny<m and image[nx][ny]==0:
                image[nx][ny]=2
                ct+=1
                q.append((nx,ny))
                
    return ct
grid = [
 [1,1,1,1,1,1],
 [1,0,0,1,1,1],
 [1,1,1,0,1,0],
 [1,1,0,1,1,0],
 [1,0,1,0,1,0]
]
print(floodFill(grid,1,1))