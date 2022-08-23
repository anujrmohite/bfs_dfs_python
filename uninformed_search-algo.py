graph = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'D'],
  'D': ['B', 'C', 'E'],
  'E': ['D']
}

def bfs(start_node,graph):
    visited=[]
    queue = [start_node]
    
    if start_node not in graph:
        print("Specified Node is not in the Graph")
        return
    
    while queue:
        current =queue.pop(0)
        print(current, end=" ")
        visited.append(current)
        
        for adj_nodes in graph[current]:
            if adj_nodes not in visited:
                visited.append(adj_nodes)
                queue.append(adj_nodes)
   
     
def dfs_iterative(start_node,graph):
    visited= set()
    if start_node not in graph:
        print("Specified Node is not in the Graph")
        return
    
    stack = []
    stack.append(start_node)
    while stack:
        current = stack.pop()  
        if current not in visited:
            print(current,end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

print("BFS")
print(graph)
bfs("A",graph)
print("\n")
print("DFS")
print(graph)
dfs_iterative("A",graph)

