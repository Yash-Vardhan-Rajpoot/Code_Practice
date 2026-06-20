def helper(n:int,k:int)->int:
    same=k
    diff=k*(k-1)
    total=same+diff
    for i in range(3,n+1):
        same=diff
        diff=total*(k-1)
        total=same+diff
    return total

n,m=map(int,input().split())
print(helper(n,m))