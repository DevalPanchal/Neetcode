class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    max_so_far = float("-inf")

    def check(node: TreeNode | None, max_so_far):
        if node is None:
            return 0
        good = 1 if node.val >= max_so_far else 0
        new_max = max(max_so_far, node.val)
        return good + check(node.left, new_max) + check(node.right, new_max)

    return check(root, max_so_far)

        
        

    
# ---------- test helper ----------

def buildTree(values):
    # Builds a tree from a level-order list, like LeetCode shows it.
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


# ---------- test cases: (input, expected number of good nodes) ----------
# A node is good if no node on the path from the root down to it is BIGGER than it.

tests = [
    ([3, 1, 4, 3, None, 1, 5], 4),            # LeetCode example 1
    ([3, 3, None, 4, 2], 3),                  # LeetCode example 2: equal values count as good
    ([1], 1),                                 # LeetCode example 3: the root is always good
    ([2, 2, 2], 3),                           # all equal, so every node is good
    ([5, 4, 3, 2, 1], 1),                     # everything is smaller than the root
    ([1, 2, 3, 4, 5, 6, 7], 7),               # every path keeps getting bigger
    ([1, None, 2, None, 3], 3),               # increasing chain down the right
    ([3, 2, None, 1], 1),                     # decreasing chain down the left
    ([9, None, 3, 6], 1),                     # 6 is bigger than its parent 3, but not bigger than 9
    ([2, None, 4, 10, 8, None, None, 4], 4),  # the bottom 4 is beaten by 8 on its path
    ([-1, -2, 0], 2),                         # negative values
]

for values, expected in tests:
    got = goodNodes(buildTree(values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")
