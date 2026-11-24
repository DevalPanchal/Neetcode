class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def invertTree(root: TreeNode | None) -> TreeNode | None:
    # 1. base case, if there is no root then return None
    if not root:
        return None

    # 2. swap root.left and root.right
    root.left, root.right = root.right, root.left

    # 3. tell left and right subtrees to invert themselves
    invertTree(root.left)
    invertTree(root.right)

    return root


# ---------- test helpers ----------

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


def treeToList(root):
    # Turns a tree back into a level-order list so it's easy to print and compare.
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:   # drop trailing Nones
        result.pop()
    return result


# ---------- test cases: (input, expected output) ----------

tests = [
    ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),     # full tree (NeetCode example)
    ([2, 1, 3], [2, 3, 1]),                             # small tree
    ([], []),                                           # empty tree
    ([1], [1]),                                         # single node
    ([1, 2], [1, None, 2]),                             # only a left child
    ([1, None, 2], [1, 2]),                             # only a right child
    ([1, 2, 3, 4, None, None, 5], [1, 3, 2, 5, None, None, 4]),  # uneven tree
]

for values, expected in tests:
    got = treeToList(invertTree(buildTree(values)))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")



