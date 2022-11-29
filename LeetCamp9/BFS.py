from collections import deque

###################################
####        BFS Vanilla        ####
###################################

def get_neighbors(node):
    # Use this function to get the neighbors of the node
    pass

def bfs(root):
    queue = deque([root])
    visited = set([root])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)


##########################################
####        BFS Level Tracking        ####
##########################################

def bfs_level(root):
    queue = deque([root])
    visited = set([root])
    level = 0 # add a level counter
    while len(queue) > 0:
        # the current queue length is the number of nodes in this level
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            for neighbor in get_neighbors(node):
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        # increment level
        level += 1
