from collections import deque
def bfs(src,graph,visited,ans):
    q=deque()
    q.append(src)
    ans.append(src)
    visited[src]=True
    while len(q)!=0:
        node=q.popleft()
        for i in graph[node]:
            if visited[i]==False:
                visited[i]=True
                q.append(i)
                ans.append(i)

def Dfs(src,graph,visited,ans):
    visited[src]=True
    ans.append(src)
    for i in graph[src]:
        if visited[i]==False:
            Dfs(i,graph,visited,ans)
def solve():
    v,n=map(int,input().split())
    edges=[]
    for i in range(n):
        a=list(map(int,input().split()))
        edges.append(a)
    graph=[[] for _ in range(v)]
    for i in range(n):
        x=edges[i][0]
        y=edges[i][1]
        graph[x].append(y)
        graph[y].append(x)
    print(graph)
    visited=[False]*v
    ans=[]
    ans1=[]
    visited1=[False]*v
    for i in range(v):
        if visited[i]==False:
            Dfs(i,graph,visited,ans)
    bfs(0,graph,visited1,ans1)
    print(ans)
    print(ans1)

solve()