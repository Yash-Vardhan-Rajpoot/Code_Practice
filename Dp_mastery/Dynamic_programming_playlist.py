def solve():
    arr=list(map(int,input().split()))
    queries=list(map(int,input().split()))
    prefix=[0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]
    ans=[]
    for i in queries:
        ans.append(prefix[i])
    return ans
print(*solve())