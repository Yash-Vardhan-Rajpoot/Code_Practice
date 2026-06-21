from math import ceil
def helper(n:int,x:int,arr:list)->int:
    ans=[]
    for i in range(n):
        ans.append(ceil(arr[i]/x))
    print(ceil(sum(arr)/x),sum(ans)) 
t=int(input())
while t>0:
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    helper(n,x,arr)
    t-=1