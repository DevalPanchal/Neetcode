from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: TreeNode | None) -> list[int]:
    res = []

    if not root:
        return res

    q = deque([root])

    while q:
        level_size = len(q)

        for i in range(level_size):
            node = q.popleft()

            # add left child to queue
            if node.left is not None:
                q.append(node.left)

            # add right child to queue
            if node.right is not None:
                q.append(node.right)

            if i == level_size - 1:
                res.append(node.val)
    return res
        



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


# ---------- test cases: (input, expected right side view) ----------
# The right side view is the LAST node you'd see on each level, looking from the right.

tests = [
    ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),        # LeetCode example 1
    ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),  # LeetCode example 2: deepest nodes are on the left
    ([1, None, 3], [1, 3]),                          # LeetCode example 3
    ([], []),                                        # LeetCode example 4: empty tree
    ([1], [1]),                                      # single node
    ([1, 2], [1, 2]),                                # only a left child, so you can see it from the right
    ([1, 2, 3, 4], [1, 3, 4]),                       # the left side is deeper than the right
    ([1, 2, 3, 4, 5, 6, 7], [1, 3, 7]),              # full tree
    ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),        # every node only has a left child
]

for values, expected in tests:
    got = rightSideView(buildTree(values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")
