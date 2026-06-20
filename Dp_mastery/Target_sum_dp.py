def solve():
    n,t=map(int,input().split())
    arr=list(map(int,input().split()))
    dp=[[0 for _ in range(t+1)] for _ in range(n+1)]
    for i in range(0,n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,t+1):
            if arr[i-1]<=j:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-arr[i-1]])
            else: dp[i][j]=dp[i-1][j]
    return dp[n][t]
print(solve())