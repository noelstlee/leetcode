class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res