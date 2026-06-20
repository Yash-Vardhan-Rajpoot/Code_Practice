def helper(n:int)->int:
    dp0=[0]*(n+1)
    dp1=[0]*(n+1)
    dp0[1]=1
    dp1[1]=1
    for i in range(2,n+1):
        dp0[i]+=dp1[i-1]
        dp1[i]+=(dp0[i-1]+dp1[i-1])
    return dp0[n]+dp1[n]
n=int(input("Enter the length of Binary->"))
print(helper(n))