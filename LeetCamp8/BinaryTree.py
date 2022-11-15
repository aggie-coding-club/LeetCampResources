from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


###############################################
####             Your Function             ####
###############################################
def yourFunction(root: TreeNode):
    pass


###############################################
####         Boilerplate Functions         ####
###############################################
# from collections import deque
def bfs(root: TreeNode, target):
    """Breadth First Search (BFS)"""
    # Initialize a queue
    q = deque()
    # If the root exists, enqueue it
    if root:
        q.append(root)

    while len(q) > 0:
        node = q.popleft()
        # If the current node is the target
        if node.val == target:
            return node
        # If the node has a left child, enqueue it
        if node.left:
            q.append(node.left)
        # If the node has a right child, enqueue it
        if node.right:
            q.append(node.right)
    # If there are no more nodes in the queue
    # and we haven't found the target, it is not in the tree
    return None


# This is how your tree is built from input
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return TreeNode(f(val), left, right)


if __name__ == "__main__":
    # Example Input: 5 4 3 x x 8 x x 6 x x
    # Reference https://tx.ag/LeetCamp8Slides
    test_case = input()  # You can hard code this or make many tests
    # test_case = "5 4 3 x x 8 x x 6 x x"
    root = build_tree(iter(test_case.split()), int)  # Change int if different type
    print(yourFunction(root))  # EDIT THIS TO BE YOUR FUNCTION NAME
