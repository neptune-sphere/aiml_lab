
graph={
    'a':['b','c','d'],
    'b':['e'],
    'c':['d','e'],
    'd':[],
    'e':[]
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        
        m = queue.pop(0)
        print(m)

        for neigh in graph[m]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)


bfs(visited,graph,'a')
