# Depth-First Search (DFS) Implementation

# Tree represented as adjacency list
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

# DFS function (recursive)
def dfs(tree, node, visited):
    # Visit the node
    visited.append(node)

    # Visit all adjacent nodes (children)
    for neighbor in tree[node]:
        if neighbor not in visited:
            dfs(tree, neighbor, visited)

# Driver code
visited_nodes = []
start_node = 1

dfs(tree, start_node, visited_nodes)

# Display result
print("DFS Traversal:")
for node in visited_nodes:
    print(node, end=" ")