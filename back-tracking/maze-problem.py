maze=[[0,1,1],[0,0,0],[0,1,0]]
sol=[[0 for _ in range(len(maze))] for _ in range(len(maze))]
N=3
global ct
ct=0
def path(x,y,sol):
    if x==N-1 and y==N-1 and sol[x][y]==0:
        sol[x][y]=1
        
        return True
    
    if x<0 or y<0 or x>=N or y>=N or maze[x][y]==1 or sol[x][y]==1:
        return False
    
    sol[x][y]=1
    if path(x+1,y,sol):
        return True
    if path(x-1,y,sol):
        return True
    if path(x,y+1,sol):
        return True
    if path(x,y-1,sol):
        return True
    sol[x][y]=0
    return False
if path(0,0,sol):
    for i in sol:
        print(i)
else:
    print("No path found")

for i in sol:
    print(i)
print(ct)