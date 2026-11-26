class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode | None, k: int) -> int:
    values = []

    def inorder(node: TreeNode | None):
        if node is None:
            return

        inorder(node.left)
        values.append(node.val)
        inorder(node.right)

    inorder(root)
    return values[k-1]


def kthSmallest2(root: TreeNode | None, k: int) -> int:
    count = 0
    ans = 0

    def inorder(node: TreeNode | None):
        nonlocal count, ans

        if node is None or count >= k:
            return None

        inorder(node.left)

        count += 1
        if count == k:
            ans = node.val
            return

        inorder(node.right)

    inorder(root)
    return ans

    

    
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


# ---------- test cases: (tree, k, expected value) ----------
# k counts from 1, so k = 1 means the smallest value.

tests = [
    ([3, 1, 4, None, 2], 1, 1),                 # LeetCode example 1
    ([5, 3, 6, 2, 4, None, None, 1], 3, 3),     # LeetCode example 2
    ([1], 1, 1),                                # single node
    ([5, 3, 6, 2, 4, None, None, 1], 1, 1),     # smallest value, deepest on the left
    ([5, 3, 6, 2, 4, None, None, 1], 6, 6),     # largest value (k = number of nodes)
    ([2, 1, 3], 3, 3),                          # largest in a small tree
    ([3, 1, 4, None, 2], 2, 2),                 # answer is the right child of a left child
    ([1, None, 2, None, 3, None, 4], 4, 4),     # every node only has a right child
    ([4, 3, None, 2, None, 1], 2, 2),           # every node only has a left child
    ([0, -3, 5, -5], 2, -3),                    # zero and negative values
]

for values, k, expected in tests:
    got = kthSmallest(buildTree(values), k)
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  k={k}  got={got}  expected={expected}")
