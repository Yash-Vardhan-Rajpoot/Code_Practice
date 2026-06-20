from collections import deque
def solve():
    v=int(input())
    Edges=[[0, 1], [1, 2], [2, 0], [2, 3]]
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
    while len(q)!=0:
        node=q.popleft()
        visited[node]=True
        for i in Graph[node]:
            if visited[i]==False:
                Indegree[i]-=1
                if Indegree[i]==0:q.append(i)
        count+=1
    if count==v: return True
    else: return False
print(solve())