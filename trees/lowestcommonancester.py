class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None

        # if n1 and n2 less than root val then navigate left subtree
        if p.val < root.val and q.val < root.val:
            return lowestCommonAncestor(root.left, p, q)

        # if n1 and n2 greater than root val then navigate right subtree
        if p.val > root.val and q.val > root.val:
            return lowestCommonAncestor(root.right, p, q)

        # if n1 and n2 are on opposite sides, then the root is the LCA
        return root


def lowestCommonAncestor2(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    node = root

    if root is None:
        return None

    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
    
        elif p.val > node.val and q.val > node.val:
            node = node.right
    
        else:
            return node

# ---------- test helpers ----------

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


def findNode(root, val):
    # p and q are real nodes in the tree, so look them up by value.
    if root is None:
        return None
    if root.val == val:
        return root
    return findNode(root.left, val) or findNode(root.right, val)


# ---------- test cases: (tree, p value, q value, expected LCA value) ----------
# This is LeetCode 235: the tree is a Binary Search Tree (left < node < right).
# A node counts as an ancestor of itself.
#
#            6
#          /   \
#         2     8
#        / \   / \
#       0   4 7   9
#          / \
#         3   5

bst = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]

tests = [
    (bst, 2, 8, 6),         # LeetCode example 1: p and q on opposite sides of the root
    (bst, 2, 4, 2),         # LeetCode example 2: p is an ancestor of q
    (bst, 8, 2, 6),         # same as example 1, but p and q swapped
    (bst, 3, 5, 4),         # both deep in the left subtree
    (bst, 0, 5, 2),         # split happens at node 2
    (bst, 0, 3, 2),         # one shallow, one deep, both left of the root
    (bst, 7, 9, 8),         # both in the right subtree
    (bst, 3, 9, 6),         # one deep on the left, one on the right
    (bst, 6, 3, 6),         # p is the root itself
    ([2, 1], 2, 1, 2),      # LeetCode example 3: tiny tree
]

for values, p_val, q_val, expected in tests:
    root = buildTree(values)
    result = lowestCommonAncestor(root, findNode(root, p_val), findNode(root, q_val))
    got = result.val if result else None
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  p={p_val}  q={q_val}  got={got}  expected={expected}")
