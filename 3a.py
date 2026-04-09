# Depth-Limited Search (DLS) Implementation

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

# DLS function
def dls(tree, node, depth_limit, current_depth, visited):
    # Visit the node
    visited.append(node)

    # Stop if depth limit reached
    if current_depth == depth_limit:
        return

    # Visit children
    for neighbor in tree[node]:
        if neighbor not in visited:
            dls(tree, neighbor, depth_limit, current_depth + 1, visited)

# Driver code
visited_nodes = []
start_node = 1
depth_limit = 2   # Change this to test different limits

dls(tree, start_node, depth_limit, 0, visited_nodes)

# Display result
print("DLS Traversal (Depth Limit =", depth_limit, "):")
for node in visited_nodes:
    print(node, end=" ")