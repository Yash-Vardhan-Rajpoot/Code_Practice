def helper(arr:list,k:int)->int:
    n=len(arr)
    bbp=[0]*(n)
    bsp=[0]*(n)
    bbp[0]=-arr[0]
    for i in range(1,n):
        bbp[i]=max(bbp[i-1],bsp[i-1]-arr[i])
        bsp[i]=max(bsp[i-1],arr[i]+bbp[i-1]-k)
    return bsp[n-1]
arr=list(map(int,input().split()))
k=int(input())
print(helper(arr,k))
