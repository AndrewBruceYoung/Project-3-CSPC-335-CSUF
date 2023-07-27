def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def convert_to_edges(adj_list):
    edges = []
    for vertex, neighbors in enumerate(adj_list):
        for neighbor, weight in neighbors:
            edges.append([vertex, neighbor, weight])
    return edges

def kruskal(edges, num_vertices):
    sorted_edges = sorted(edges, key=lambda x: x[2])  # Sort edges by weight in ascending order
    parent = [i for i in range(num_vertices)]
    rank = [0 for _ in range(num_vertices)]
    min_spanning_tree = []

    for edge in sorted_edges:
        u, v, weight = edge

        if find(parent, u) != find(parent, v):  # Check if adding this edge creates a cycle
            min_spanning_tree.append([[u, v], weight])
            union(parent, rank, u, v)

    # Convert min_spanning_tree to the adjacency list representation
    adj_list = [[] for _ in range(num_vertices)]
    for edge in min_spanning_tree:
        u, v = edge[0]
        weight = edge[1]
        adj_list[u].append([v, weight])
        adj_list[v].append([u, weight])

    return adj_list

# Sample Input
adj_list = [
    [[1, 3], [2, 5]],
    [[0, 3], [2, 10], [3, 12]],
    [[0, 5], [1, 10]],
    [[1, 12]]
]
num_vertices = 4

# Convert the adjacency list to the edges format
edges = convert_to_edges(adj_list)

# Sample Output
result = kruskal(edges, num_vertices)
print(result)
