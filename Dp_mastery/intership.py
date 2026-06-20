def solve():
    n=int(input())
    arr=[]
    for i in range(n):
        a=list(map(int,input().split()))
        arr.append(a)
    dpE=[0]*n
    dpH=[0]*n
    dpN=[0]*n
    dpE[0]=arr[0][0]
    dpH[0]=arr[0][1]
    dpN[0]=0
    for i in range(1,n):
        dpE[i]=arr[i][0]+max(dpE[i-1],dpH[i-1],dpN[i-1])
        dpH[i]=arr[i][1]+dpN[i-1]
        dpN[i]=max(dpE[i-1],dpH[i-1],dpN[i-1])
    print(max(dpE[n-1],dpH[n-1],dpN[n-1]))
solve()