# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # checks if two trees are identical
        def sameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return (sameTree(a.left, b.left) and sameTree(a.right, b.right))

        if not subRoot:
            return True
        if not root:
            return False
        
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            # possible subtree root found
            if node.val == subRoot.val:
                if sameTree(node, subRoot):
                    return True
            stack.append(node.left)
            stack.append(node.right)

        return False