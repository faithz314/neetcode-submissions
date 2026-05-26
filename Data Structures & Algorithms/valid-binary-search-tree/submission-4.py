# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #inorder tree walk??

        def tree_walk(root, result):
            if root != None:
                tree_walk(root.left, result)
                result.append(root.val)
                tree_walk(root.right, result)
        
        

        inorder_values = []
        tree_walk(root, inorder_values)

        # Now, check if the inorder values are strictly increasing
        for i in range(1, len(inorder_values)):
            if inorder_values[i] <= inorder_values[i - 1]:
                return False

        return True








        # if not root:
        #     return True

        # q = deque([(root, float("-inf"), float("inf"))])

        # while q:
        #     node, left, right = q.popleft()
        #     if not (left < node.val < right):
        #         return False
        #     if node.left:
        #         q.append((node.left, left, node.val))
        #     if node.right:
        #         q.append((node.right, node.val, right))

        # return True