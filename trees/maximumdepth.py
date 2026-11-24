class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode | None) -> int:
    # return 0 if there is no root
    if not root:
        return 0

    # 1. depth at left and right root, each root visited is counts as one then we keep checking
    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)

    # 3. return the maximum value of either left or right height
    return 1 + max(leftHeight, rightHeight)



'''
    6
   / \
  3   4
 /
2
'''


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


# ---------- test cases: (input, expected depth) ----------

tests = [
    ([1, 2, 3, None, None, 4], 3),          # NeetCode example
    ([6, 3, 4, 2], 3),                      # the tree drawn above
    ([], 0),                                # empty tree
    ([1], 1),                               # single node
    ([1, 2], 2),                            # only a left child
    ([1, None, 2], 2),                      # only a right child
    ([1, 2, 3, 4, 5, 6, 7], 3),             # full tree
    ([1, 2, None, 3, None, 4], 4),          # every node only has a left child
    ([1, None, 2, None, 3], 3),             # every node only has a right child
    ([1, 2, 3, None, None, 4, None, 5], 4), # deepest path is on the right side
]

for values, expected in tests:
    got = maxDepth(buildTree(values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")