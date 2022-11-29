###################################
####        DFS Vanilla        ####
###################################

def get_neighbors(node):
    # Use this function to get the neighbors of the node
    pass

def dfs(root, visited):
    # root is a node, visited is a set
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs(neighbor, visited)
