from collections import Counter
directions=[[0,-1],[0,1],[-1,0],[1,0]]
def dfs(grid,i,j,val,maxi,count):
    temp=val
    count+=temp
    maxi[0]=max(maxi[0],count)
    grid[i][j]=0
    for dir in directions:
        n_i=i+dir[0]
        n_j=j+dir[1]
        if n_i>=0 and n_j>=0 and n_i<len(grid) and n_j<len(grid[0]) and grid[n_i][n_j]!=0:
            dfs(grid,n_i,n_j,grid[n_i][n_j],maxi,count)
    grid[i][j]=temp


def solve():
    grid=[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    maxi=[-10**18]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]!=0:
                count=0
                dfs(grid,i,j,grid[i][j],maxi,count)
    return maxi[0]
print(solve())