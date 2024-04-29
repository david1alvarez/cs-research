# sample graph implemented as a dictionary
graph = {'A': set(['B', 'C', 'E']),
         'B': set(['A','D', 'E']),
         'C': set(['A', 'F', 'G']),
         'D': set(['B']),
         'E': set(['A', 'B','D']),
         'F': set(['C']),
         'G': set(['C'])}

visited = set()

def dfs_connected_component(graph, start, visited=None):
    if visited is None:
        visited = list()
    visited.add(start)
    print(visited)
    for next in (graph[start] - visited): # remove `visited` set from the set of nodes at `graph[start]`
        dfs_connected_component(graph, next, visited)
    return visited

print(dfs_connected_component(graph, 'C')) #{'E', 'D', 'C', 'F', 'B', 'G', 'A'}

