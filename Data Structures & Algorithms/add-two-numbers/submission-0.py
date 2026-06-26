# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        p3 = l3 = ListNode()

        overflow = 0
        while p1 or p2 or overflow:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0

            subRes = val1 + val2 + overflow
            overflow = subRes // 10
            subRes = subRes % 10

            l3.next = ListNode(subRes)
            l3 = l3.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            
        return p3.next
            
