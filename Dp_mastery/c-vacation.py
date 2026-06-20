def solve():
    n=int(input())
    arr=[]
    for i in range(n):
        a=list(map(int,input().split()))
        arr.append(a)
    dp=[0]*(n)
    dp[0]=max(arr[0])
    curr=0
    for i in range(len(arr[0])):
        if arr[0][i]==dp[0]: 
            curr=i
            break
    for i in range(1,n):
        if curr==0:
            if arr[i][1]>=arr[i][2]:
                dp[i]=dp[i-1]+arr[i][1]
                curr=1
            else:
                dp[i]=dp[i-1]+arr[i][2]
                curr=2
        elif curr==1:
            if arr[i][0]>=arr[i][2]:
                dp[i]=dp[i-1]+arr[i][0]
                curr=0
            else:
                dp[i]=dp[i-1]+arr[i][2]
                curr=2
        else:
            if arr[i][1]>=arr[i][0]:
                dp[i]=dp[i-1]+arr[i][1]
                curr=1
            else:
                dp[i]=dp[i-1]+arr[i][0]
                curr=0
    return dp[n-1]
print(solve())