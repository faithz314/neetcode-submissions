# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if p and q and p.val == q.val:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # else:
        #     return False

        # how about iterative bfs
        queue1 = [p]
        queue2 = [q]
        while queue1 and queue2:
            curP = queue1.pop()
            curQ = queue2.pop()
            if not curP and not curQ:
                continue

            if not curP or not curQ:
                return False

            if curP.val != curQ.val:
                return False
            else:
                queue1.append(curP.left)
                queue1.append(curP.right)
                queue2.append(curQ.left)
                queue2.append(curQ.right)
        return True

