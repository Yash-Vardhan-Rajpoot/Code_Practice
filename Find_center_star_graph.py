def solve():
    v=int(input("Enter the number of vertex->"))
    n=int(input("Enter the number of Edges->"))
    Edges=[]
    for i in range(n):
        x,y=map(int,input().split())
        Edges.append([x,y])
    Graph=[[] for _ in range(v)]
    for i in range(n):
        x=Edges[i][0]
        y=Edges[i][1]
        Graph[x].append(y)
        Graph[y].append(x)
    for i in range(v):
        if len(Graph[i])==len(Edges): return i
    
print(solve())