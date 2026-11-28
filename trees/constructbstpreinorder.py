def buildTree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    idx_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def helper(left: int, right: int) -> TreeNode | None:
        nonlocal pre_idx
        # 1. Base case: if left > right, this subtree is empty -> return None

        # 2. Pick root_val = preorder[pre_idx], increment pre_idx, create TreeNode(root_val)

        # 3. Look up mid = idx_map[root_val]

        # 4. Build root.left (left to mid - 1) and root.right (mid + 1 to right)
        #    (Order matters here! Why must root.left be built before root.right?)

        # 5. Return root
        pass

    return helper(0, len(inorder) - 1)