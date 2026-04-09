from collections import deque

# Tree as adjacency list
tree = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [],
    5: [],
    6: [],
    7: []
}

def bfs(tree, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)

            for neighbor in tree[node]:
                queue.append(neighbor)

    return visited

# Run BFS
bfs_result = bfs(tree, 1)

print("BFS Traversal:")
print(*bfs_result)