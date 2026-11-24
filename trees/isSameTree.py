class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode | None, q: TreeNode | None) -> bool:
    # empty case
    if p is None and q is None: 
        return True

    # only one empty
    if p is None or q is None:
        return False

    # values are different
    if p.val != q.val:
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    


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


# ---------- test cases: (tree p, tree q, expected result) ----------
# Same tree means: same shape AND same value in every matching spot.

tests = [
    ([1, 2, 3], [1, 2, 3], True),                   # NeetCode example 1
    ([4, 7], [4, None, 7], False),                  # NeetCode example 2: 7 is on different sides
    ([1, 2, 3], [1, 3, 2], False),                  # same values, swapped children
    ([], [], True),                                 # both empty
    ([1], [], False),                               # only q is empty
    ([], [1], False),                               # only p is empty
    ([1], [1], True),                               # single matching node
    ([1], [2], False),                              # single node, different values
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True),       # bigger matching trees
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 6], False),      # only a deep value differs
    ([1, 2, 3, 4], [1, 2, 3, None, 4], False),      # only the deep shape differs
    ([0, 0], [0, 0], True),                         # values of 0 still count as real nodes
]

for p_values, q_values, expected in tests:
    got = isSameTree(buildTree(p_values), buildTree(q_values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  p={p_values}  q={q_values}  got={got}  expected={expected}")