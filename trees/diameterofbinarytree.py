class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: TreeNode | None) -> int:
    max_diameter = 0

    def dfs(node: TreeNode | None) -> int:
        nonlocal max_diameter
        # 1. Base case
        if not node:
            return 0
        # 2. Get left and right heights
        left = dfs(node.left)
        right = dfs(node.right)
        # 3. Update max_diameter (hint: in Python, use `nonlocal max_diameter`)
        max_diameter = max(max_diameter, right + left)
        # 4. Return THIS node's height to its parent
        return 1 + max(left, right)

    dfs(root)
    return max_diameter


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


# ---------- test cases: (input, expected diameter) ----------
# The diameter counts EDGES (the lines between nodes), not nodes.

tests = [
    ([1, None, 2, 3, 4, 5], 3),                 # NeetCode example
    ([1, 2, 3, 4, 5], 3),                       # longest path goes through the root: 4-2-1-3
    ([], 0),                                    # empty tree
    ([1], 0),                                   # single node, no edges
    ([1, 2], 1),                                # one edge
    ([1, 2, 3], 2),                             # left-root-right
    ([1, 2, 3, 4, 5, 6, 7], 4),                 # full tree
    ([1, 2, None, 3, None, 4], 3),              # every node only has a left child
    ([1, 2, None, 3, 4, 5, None, None, 6], 4),  # longest path does NOT go through the root: 5-3-2-4-6
]

for values, expected in tests:
    got = diameterOfBinaryTree(buildTree(values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")

