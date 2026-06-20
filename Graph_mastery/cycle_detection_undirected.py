from collections import deque
def iscyclic(src,visited,Graph):
    q=deque()
    q.append((src,-1))
    visited[src]=True
    while len(q)!=0:
        node,parent=q.popleft()
        for n in Graph[node]:
            if visited[n]==False:
                visited[n]=True
                q.append((n,node))
            elif n!=parent: return True
    return False
def solve():
    v=int(input("Enter the number of vertexs->"))
    n=int(input("Enter the number of edges->"))
    print("Enter the edges->")
    Edges=[]
    for i in range(n):
        x,y=map(int,input().split())
        Edges.append([x,y])
    Graph=[[] for _ in range(v)]
    for i in range(n):
        Graph[Edges[i][0]].append(Edges[i][1])
        Graph[Edges[i][1]].append(Edges[i][0])
    visited=[False]*v
    for i in range(v):
        if visited[i]==False:
            ans=iscyclic(i,visited,Graph)
            if ans==True:
                print("true")
                return
    print("False")
    
solve()