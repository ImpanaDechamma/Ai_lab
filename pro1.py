def dls(tree, node, depth, visited):
    """Depth-Limited Search engine."""
    visited.append(node)
    if depth <= 0:
        return
    
    if node in tree:
        for child in tree[node]:
            dls(tree, child, depth - 1, visited)

def iddfs_from_user():
    tree = {}
    
    # 1. Get Tree Structure from User
    print("--- Tree Construction ---")
    nodes_count = int(input("How many parent nodes (nodes with children) are there? "))
    
    for _ in range(nodes_count):
        parent = int(input("\nEnter parent node: "))
        children = list(map(int, input(f"Enter children for node {parent} (separated by space): ").split()))
        tree[parent] = children

    # 2. Get Search Parameters
    root_node = int(input("\nEnter the starting (root) node: "))
    max_depth = int(input("Enter the maximum depth to search: "))

    # 3. Perform IDDFS
    print("\n--- IDDFS Execution Results ---")
    for d in range(max_depth + 1):
        visited_nodes = []
        dls(tree, root_node, d, visited_nodes)
        print(f"Depth Limit {d}: Visited nodes {visited_nodes}")

if __name__ == "__main__":
    iddfs_from_user()