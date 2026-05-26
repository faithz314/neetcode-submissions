# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # first define the easy function to sort two linked lists
        def sort_two_lists(list1, list2):
            node1 = list1
            node2 = list2
            node3 = list3 = ListNode(0)
            while node1 and node2:
                if node1.val < node2.val:
                    node3.next = node1
                    node1= node1.next
                else:
                    node3.next = node2
                    node2= node2.next
                node3=node3.next
            node3.next = node1 or node2
            return list3.next
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                if (i+1) < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None
                mergedList = sort_two_lists(lists[i], l2)
                mergedLists.append(mergedList)
            lists = mergedLists
        return lists[0]

                

                

        