def solve():
    n=int(input("Enter the number of elements->"))
    c=int(input("Enter the capacity->"))
    wt=[]
    val=[]
    for i in  range(n):
        v,w=map(int,input().split())
        wt.append(w)
        val.append(v)
    dp=[0]*(c+1)
    for i in range(c+1):
        for j in range(n):
            if wt[j]<=i:
                dp[i]=max(dp[i],val[j]+dp[i-wt[j]])
    return dp[c]

print(solve())