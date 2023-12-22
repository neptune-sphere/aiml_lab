
graph={
    'a':['b','c','d'],
    'b':['e'],
    'c':['d','e'],
    'd':[],
    'e':[]
}

visited=set()

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node)

        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)


dfs(visited,graph,'a')
        