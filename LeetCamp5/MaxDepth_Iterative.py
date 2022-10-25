class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


###############################################
####        Max Depth Iterative DFS        ####
###############################################
def maxDepth(root: TreeNode):
    if root is None:
        return 0

    depth = 0
    max_depth = 0

    stack = []
    curr = root
    prev = None
    while stack or curr is not None:  # while stack isn't empty OR curr isn't None
        if curr is not None:
            depth += 1  # Add 1 to the current depth
            stack.append(curr)  # append curr node to stack
            curr = curr.left  # update curr node to curr.left
        else:
            if (
                depth > max_depth
            ):  # If the current depth is greater than any other path found so far
                max_depth = depth  # update max_depth
                depth = 0  # reset current depth
            prev = stack.pop()  # pop node off of stack
            curr = prev.right  # update curr to prev.right
    return max_depth


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
    print(maxDepth(root))  # EDIT THIS TO BE YOUR FUNCTION NAME
