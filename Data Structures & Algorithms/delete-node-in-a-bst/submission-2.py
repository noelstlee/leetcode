# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        
        # searching
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # simple cases when root has 0 or 1 child node; we return the remaining subtree (node)
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else: # difficult case when root has 2 children; we substitue with the min node in the right subtree
                minNode = self.findMinNode(root.right)
                root.val = minNode.val # substitution with min node
                root.right = self.deleteNode(root.right, minNode.val) # now after substituting, we delete that node
        return root

    def findMinNode(self, root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        
        