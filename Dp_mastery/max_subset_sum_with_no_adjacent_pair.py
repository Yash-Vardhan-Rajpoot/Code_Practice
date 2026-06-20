def solve():
    arr=list(map(int,input().split()))
    dp=[0]*len(arr)
    dp[0]=max(0,arr[0])
    dp[1]=max(0,arr[0],arr[1])
    for i in range(2,len(arr)):
        dp[i]=max(0,dp[i-1],dp[i-2]+arr[i])
    print(dp)
    return dp[len(arr)-1]
print(solve())

# [2,-3, 5, -8, 7] the best ans come hair is (2,5,7)=14