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
def dfsRecursive(root: TreeNode, target):
    """Recursive Depth First Search (DFS)"""
    if root is None:  # Base Case
        return
    elif root.val == target:  # root is target
        return root

    return dfsRecursive(root.left, target) or dfsRecursive(root.right, target)


def dfsIterative(root: TreeNode, target):
    """Iterative Depth First Search (DFS)"""
    if root is None:
        return
    stack = []
    curr = root
    prev = None
    while stack or curr is not None:  # While stack isn't empty OR curr isn't None
        if curr is not None:
            if curr.val == target:  # if curr node is target, return it
                return curr
            stack.append(curr)  # append curr node to stack
            curr = curr.left  # update curr node to curr.left
        else:
            prev = stack.pop()  # pop node off of stack
            curr = prev.right  # update curr to prev.right
    return  # target is not in the tree


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
    # Reference https://tx.ag/LeetCamp5Slides
    test_case = input()  # You can hard code this or make many tests
    # test_case = "5 4 3 x x 8 x x 6 x x"
    root = build_tree(iter(test_case.split()), int)  # Change int if different type
    print(dfsIterative(root, 6))  # EDIT THIS TO BE YOUR FUNCTION NAME
