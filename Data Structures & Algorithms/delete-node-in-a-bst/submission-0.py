class Solution:
    def minValueNode(self, root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # when found
            if not root.left: # connect the root with the right subtree
                return root.right
            elif not root.right: # connect the root with the left subtree
                return root.left 
            else: # when it is in the middle
                minNode = self.minValueNode(root.right)
                # substitute
                root.val = minNode.val
                root.right = self.deleteNode(root.right, root.val)
        return root