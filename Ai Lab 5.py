'''
# Graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'F'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': ['C', 'E']
}

# Function to find a path using DFS + backtracking
def find_path(graph, start, end, path=[]):
    path = path + [start]                # add start node to the current path
    if start == end:                     # if start == end, we found a path
        return path
    if start not in graph:               # if start node has no neighbors
        return None
    for node in graph[start]:            # explore each neighbor
        if node not in path:             # avoid cycles
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath           # return first path found
    return None                          # no path found

# Sample run
print(find_path(graph, 'A', 'D'))  # Example query
print(find_path(graph, 'C', 'E'))  # Example query
print(find_path(graph, 'A', 'F'))  # Example query
print(find_path(graph, 'D', 'F'))  # Example query
'''

'''
#Task 1
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'F'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': ['C', 'E']
}

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]   # add start node to current path
    if start == end:
        return path        
    if start not in graph:
        return None        
    shortest = None
    for node in graph[start]:
        if node not in path:   
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if shortest is None or len(newpath) < len(shortest):
                    shortest = newpath  
    return shortest

print(find_shortest_path(graph, 'A', 'D'))
print(find_shortest_path(graph, 'A', 'F'))
print(find_shortest_path(graph, 'A', 'E'))
'''

'''
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1, 'F': 3},
    'D': {'C': 1, 'E': 4},
    'E': {'F': 3},
    'F': {'C': 1, 'E': 2}
}

def find_shortest_path(graph, start, end, path=[], cost=0):
    path = path + [start]
    if start == end:
        return path, cost
    if start not in graph:
        return None

    shortest = None
    for node, edge_cost in graph[start].items():
        if node not in path:
            result = find_shortest_path(graph, node, end, path, cost + edge_cost)
            if result:
                if shortest is None or result[1] < shortest[1]:
                    shortest = result
    return shortest

path, cost = find_shortest_path(graph, 'A', 'E')
print("Shortest Path:", path)
print("Total Cost:", cost)
'''
import matplotlib.pyplot as plt

#Data
feature1 = [12, 11, 8, 6, 9, 6, 10]
feature2 = [4, 5, 1, 4, 3, 6, 2]

#Bubble size
sizes = [f * 20 for f in feature1]  

#Bubble chart
plt.scatter(feature1, feature2, s=sizes, c='blue', alpha=1, edgecolors='black')

plt.title("Bubble Chart of Feature 1 vs Feature 2")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()
