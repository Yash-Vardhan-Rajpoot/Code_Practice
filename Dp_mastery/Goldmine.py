def solve():
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        a=list(map(int,input().split()))
        arr.append(a)
    dp=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        dp[i][m-1]=arr[i][m-1]
    for j in range(m-2,-1,-1):
        dp[0][j]=max(dp[0][j+1],dp[1][j+1])+arr[0][j]
    for j in range(m-2,-1,-1):
        dp[n-1][j]=max(dp[n-1][j+1],dp[n-2][j+1])+arr[n-1][j]
    for i in range(1,n-1):
        for j in range(m-2,-1,-1):
            dp[i][j]=max(dp[i][j+1],dp[i+1][j+1],dp[i-1][j+1])+arr[i][j]
    maxi=-1
    for i in range(n):
        maxi=max(maxi,dp[i][0])
    print(dp)
    return maxi 
    
print(solve())

