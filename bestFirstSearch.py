# Dfs


# graph = {
#     '5' : ['3' , '7'],
#     '3' : ['2', '4'],
#     '7' : ['8'],
#     '2' : [],
#     '4' : ['8'],
#     '8' : []
# }

# visited = []
# def dfs(visited , graph , node):
#     if node not in visited :
#         print(node, end = " ")
#         visited.append(node)
#         for neighbor in graph[node]:
#             dfs(visited , graph , neighbor)

# dfs(visited , graph , '5')






# Best_first_search


from queue import PriorityQueue

v = 14

graph = [[] for i in range(v)]

def bfs(actual_src , target , n):
    visited = [False]*n
    pq = PriorityQueue()
    pq.put((0, actual_src))
    visited[actual_src] = True

    while pq.empty() == False:
        u = pq.get()[1]
        print(u , end=" ")
        if u == target:
            break
        for v,c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c,v))

print()

def addEdge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))

addEdge(0,1,3)
addEdge(0,2,6)
addEdge(0,3,5)
addEdge(1,4,9)
addEdge(1,5,8)
addEdge(2,6,12)
addEdge(2,7,14)
addEdge(3,8,7)
addEdge(8,9,5)
addEdge(8,10,6)
addEdge(9,11,1)
addEdge(9,12,10)
addEdge(9,13,2)

current_src = 0
target = 9
bfs(current_src , target ,v)


# bfs


# graph = {
#     '5' : ['3' , '7'],
#     '3' : ['2', '4'],
#     '7' : ['8'],
#     '2' : [],
#     '4' : ['8'],
#     '8' : []
# }

# visited = []
# queue = []

# def bfs(visited , graph , node):
#     visited.append(node)
#     queue.append(node)

#     while queue:
#         m = queue.pop(0)
#         print(m , end=" ")
#         for neighbors in graph[m]:
#             if neighbors not in visited:
#                 visited.append(neighbors)
#                 queue.append(neighbors)

# bfs(visited , graph , '5')