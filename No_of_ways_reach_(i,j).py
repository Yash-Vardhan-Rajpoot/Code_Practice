def solve():
    n,m=map(int,input().split())
    arr=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i==0 or j==0:
                arr[i][j]=1
            else: arr[i][j]=arr[i-1][j]+arr[i][j-1]+arr[i-1][j-1]
    return arr[n-1][m-1]
print(solve()) 