# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use Euclidian algorithm
        def gcd(val1, val2):
            greater = max(val1, val2)
            lesser = min(val1, val2)
            
            while greater % lesser != 0:
                remainder = greater % lesser
                greater = lesser
                lesser = remainder
            
            return lesser
    
        if not head or not head.next:
            return head

        p1 = head
        p2 = head.next

        while p2:
            val1 = p1.val
            val2 = p2.val
            best = gcd(val1, val2)
            p1.next = ListNode(best, p2)
            p1 = p1.next.next
            p2 = p2.next

        return head


        