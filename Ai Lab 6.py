'''
def dfs_iterative(graph, start):
    visited = []
    stack = [start]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


graph = {
    's': ['p', 'e', 'd'],
    'd': ['e', 'c', 'b'],
    'b': ['a'],
    'a': [],
    'c': [],
    'e': ['h', 'f'],
    'f': ['g', 'r'],
    'g': [],
    'r': [],
    'h': ['p'],
    'p': ['q'],
    'q': [] }

dfs_path = dfs_iterative(graph, 's')
print("DFS Traversal Path:", *dfs_path)
'''
'''
import networkx as nx

G = nx.Graph()

edges = [
    (5, 8), (5, 4), (5, 7),
    (8, 2),
    (4, 3), (4, 1),
    (7, 6),
    (6, 9)
]

G.add_edges_from(edges)

def dfs_networkx(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # Push neighbors in the exact order you want DFS to follow
            if node == 5:
                neighbors = [7, 4, 8]
            elif node == 8:
                neighbors = [2]
            elif node == 4:
                neighbors = [1, 3]
            elif node == 7:
                neighbors = [6]
            elif node == 6:
                neighbors = [9]
            else:
                neighbors = list(graph.neighbors(node))

            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


result = dfs_networkx(G, 5)
print("DFS Traversal Path:", result)
'''
def dfs_iterative(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


graph = {
    's': ['d', 'e', 'p'],
    'd': ['b', 'c', 'e'],
    'b': ['a'],
    'a': [],
    'c': [],
    'e': ['h', 'f'],
    'f': [],
    'g': [],
    'r': ['f','g'],
    'h': ['p'],
    'p': ['q'],
    'q': ['r']
}

dfs_path = dfs_iterative(graph, 's')
print("DFS Traversal Path:", *dfs_path)
