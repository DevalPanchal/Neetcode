class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
      5
    /   \
    1   7
       / \
      4   8   <-- INVALID! 4 is less than 7, so 7 is happy,
                but 4 is in 5's RIGHT subtree, so 4 MUST be > 5!
'''


def isValidBST(root: TreeNode | None) -> bool:

    def check(node: TreeNode | None, low, high):
        # if empty then return true
        if node is None:
            return True
        # if the current node value is not between low and high
        if not (low < node.val < high):
            return False
        # check left node and right node with updated values
        return check(node.left, low, node.val) and check(node.right, node.val, high)

    # run check between -inf and inf
    return check(root, float("-inf"), float("inf"))

    

    


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


# ---------- test cases: (input, expected result) ----------
# Valid BST: EVERY node in the left subtree is smaller, and EVERY node in the
# right subtree is bigger, at every level. Equal values are not allowed.

tests = [
    ([2, 1, 3], True),                                  # LeetCode example 1
    ([5, 1, 4, None, None, 3, 6], False),               # LeetCode example 2: 4 is on the right of 5 but smaller
    ([5, 1, 7, None, None, 4, 8], False),               # the tree drawn above: 4 is fine under 7, but not under 5
    ([], True),                                         # empty tree
    ([1], True),                                        # single node
    ([3, 1, 5, 0, 2, 4, 6], True),                      # full valid tree
    ([2, 2, 2], False),                                 # equal values are not allowed
    ([1, 1], False),                                    # left child equal to its parent
    ([0, -1], True),                                    # zero and negatives
    ([0, None, -1], False),                             # right child smaller than its parent
    ([10, 5, 15, None, None, 6, 20], False),            # 6 is deep on the right, but smaller than the root 10
    ([32, 26, 47, 19, None, None, 56, None, 27], False),  # 27 is deep on the left, but bigger than 26
    ([-2147483648], True),                              # smallest 32-bit value
    ([2147483647], True),                               # largest 32-bit value
]

for values, expected in tests:
    got = isValidBST(buildTree(values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")
