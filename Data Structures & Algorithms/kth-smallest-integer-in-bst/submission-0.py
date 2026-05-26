# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #im thinking in order tree traversal again and then looping but whatever

        def tree_walk(root, result):
            if root != None:
                tree_walk(root.left, result)
                result.append(root.val)
                tree_walk(root.right, result)
        
        result = []
        tree_walk(root, result)

        result.sort()

        return result[k-1]




