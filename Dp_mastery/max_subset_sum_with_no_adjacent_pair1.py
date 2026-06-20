def solve():
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    dp=[0]*len(a)
    dp[0]=max(a[0],b[0],dp[0])
    dp[1]=max(max(a[1],b[1]),dp[0],dp[1])
    for i in range(2,len(a)):
        dp[i]=max(max(a[i],b[i])+dp[i-2],dp[i-1],dp[i])
    print(dp)
    return dp[len(a)-1]
print(solve())
