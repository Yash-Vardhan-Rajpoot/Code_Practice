def helper(n:int,arr:list)->int:
    dpr=[0]*n
    dpb=[0]*n
    dpg=[0]*n
    dpr[0]=arr[0][0]
    dpb[0]=arr[0][1]
    dpg[0]=arr[0][2]
    for i in range(1,n):
        dpr[i]=arr[i][0]+min(dpb[i-1],dpg[i-1])
        dpb[i]=arr[i][1]+min(dpr[i-1],dpg[i-1])
        dpg[i]=arr[i][2]+min(dpr[i-1],dpb[i-1])
    return min(dpr[n-1],dpb[n-1],dpg[n-1])
n=int(input())
arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)
print(helper(n,arr))