from collections import deque

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def levelOrder(root: Node):
    res = []

    if not root:
        return res

    q = deque([root])

    while q:
        level_size = len(q)
        level = []

        for i in range(level_size):
            # get front node and remove from queue
            node = q.popleft()

            # add current node to the result
            level.append(node.data)

            # add left child to the queue
            if node.left is not None:
                q.append(node.left)

            # add right child to the queue
            if node.right is not None:
                q.append(node.right)

        res.append(level)

    return res


# ---------- test helper ----------

def buildTree(values):
    # Builds a tree from a level-order list, like LeetCode shows it.
    # None means "no node here", e.g. [1, None, 2] is 1 with only a right child 2.
    if not values:
        return None
    root = Node(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


# ---------- test cases: (input, expected levels) ----------
# LeetCode 102 wants one inner list per level, from top to bottom, left to right.

tests = [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),  # LeetCode example 1
    ([1], [[1]]),                                             # LeetCode example 2: single node
    ([], []),                                                 # LeetCode example 3: empty tree
    ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]]),     # full tree
    ([1, 2, None, 3, None, 4], [[1], [2], [3], [4]]),         # every node only has a left child
    ([1, None, 2, None, 3], [[1], [2], [3]]),                 # every node only has a right child
    ([1, 2, 3, 4, None, None, 5], [[1], [2, 3], [4, 5]]),     # gap in the middle of a level
    ([1, 2, 3, None, 4, 5], [[1], [2, 3], [4, 5]]),           # children on the "inside" edges
    ([0, -1, 1], [[0], [-1, 1]]),                             # zero and negative values
]

for values, expected in tests:
    got = levelOrder(buildTree(values))
    status = "PASS" if got == expected else "FAIL"
    print(f"{status}  input={values}  got={got}  expected={expected}")


