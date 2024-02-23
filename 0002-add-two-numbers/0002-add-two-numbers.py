# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        res = head
        add = 0
        
#         while l1 != None and l2 != None:
#             val = (l1.val + l2.val + add) % 10
#             add = 1 if l1.val + l2.val + add >= 10 else 0 
#             new = ListNode(val)
#             res.next = new
#             res = res.next

#             l1 = l1.next
#             l2 = l2.next
            
#         while l1 is not None:
#             val = (l1.val + add) % 10
#             add = 1 if l1.val + add >= 10 else 0
#             new = ListNode(val)
#             res.next = new
#             res = res.next
#             l1 = l1.next
#         while l2 is not None:
#             val = (l2.val + add) % 10
#             add = 1 if l2.val + add >= 10 else 0
#             new = ListNode(val)
#             res.next = new
#             res = res.next
#             l2 = l2.next
            
#         if add:
#             new = ListNode(1)
#             res.next = new
#             res = res.next
        
        while l1 is not None or l2 is not None or add != 0:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            
            val = (val1 + val2 + add) % 10
            add = (val1 + val2 + add) // 10
            new = ListNode(val)
            res.next = new
            res = res.next
            
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            
        return head.next
        