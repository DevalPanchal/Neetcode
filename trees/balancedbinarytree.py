class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode | None) -> bool:
    balanced = True

    def dfs(node) -> int:
        nonlocal balanced
        if not node:
            return 0

        # get height of left and right subtrees
        left = dfs(node.left)

        if not balanced:
            return 0
        
        right = dfs(node.right)

        # check if its balanced
        if abs(left - right) > 1:
            balanced = False

        return 1 + max(left, right)

    dfs(root)
    return balanced


# ---------- test helper ----------

def buildTree(values):
    # Builds a tree from a level-order list, like NeetCode/LeetCode show it.
    # None means "no node here", e.g. [1, None, 2] is 1 with only a right child 2.
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# ---------- test cases: (input, expected result) ----------
# Balanced means: at EVERY node, the left and right heights differ by at most 1.

tests = [
    ([1, 2, 3, None, None, 4], True),                       # NeetCode example 1
    ([1, 2, 3, None, None, 4, None, 5], False),             # NeetCode example 2
    ([], True),                                             # empty tree
    ([1], True),                                            # single node
    ([1, 2], True),                                         # one child, heights differ by 1
    ([1, 2, None, 3], False),                               # chain of 3 nodes down the left
    ([1, 2, 3, 4, 5, 6, 7], True),                          # full tree
    ([1, 2, 3, 4, 5, None, 6, 7], True),                    # uneven, but never off by more than 1
    ([1, 2, 3, 4, None, None, 5, 6, None, None, 7], False), # root looks balanced, but nodes 2 and 3 aren't
    ([1, 2, 3, 4, 5, 6, None, None, None, None, None, 7], False),  # only the RIGHT subtree (node 3) is unbalanced
]

for values, expected in tests:
    got = isBalanced(buildTree(values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")

    