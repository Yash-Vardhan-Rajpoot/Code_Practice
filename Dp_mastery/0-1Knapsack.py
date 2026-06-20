def solve():
    n=int(input())
    c=int(input())
    profit=[]
    weight=[]
    for i in range(n):
        w,p=map(int,input().split())
        profit.append(p)
        weight.append(w)
    dp=[[0 for _ in range(c+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,c+1):
            if weight[i-1]>j: dp[i][j]=dp[i-1][j]
            else: dp[i][j]=max(dp[i-1][j],profit[i-1]+dp[i-1][j-weight[i-1]])
    return dp[n][c]
print(solve())
