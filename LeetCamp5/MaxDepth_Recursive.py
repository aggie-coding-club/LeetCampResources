class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


###############################################
####        Max Depth Recursive DFS        ####
###############################################
def maxDepth(root: TreeNode):
    return 0 if root is None else 1 + max(maxDepth(root.left), maxDepth(root.right))


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
