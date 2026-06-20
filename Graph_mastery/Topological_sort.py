from collections import deque
def solve():
    v=int(input())
    Edges=[[3, 0], [1, 0], [2, 0]]
    Graph=[[] for _ in range(v)]
    for i in range(len(Edges)):
        x=Edges[i][0]
        y=Edges[i][1]
        Graph[x].append(y)
    visited=[False]*v
    Indegree=[0]*v
    for i in range(v):
        for j in Graph[i]:
            Indegree[j]+=1
    q=deque()
    for i in range(v):
        if Indegree[i]==0: q.append(i)
    count=0
    ans=[]
    while len(q)!=0:
        node=q.popleft()
        ans.append(node)
        visited[node]=True
        for i in Graph[node]:
            if visited[i]==False:
                Indegree[i]-=1
                if Indegree[i]==0:q.append(i)
    return ans
    
print(solve())