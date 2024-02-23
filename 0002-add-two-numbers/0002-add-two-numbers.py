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
        
        while l1 != None and l2 != None:
            val = (l1.val + l2.val + add) % 10
            print("VAL", val)
            add = 1 if l1.val + l2.val + add >= 10 else 0 
            new = ListNode(val)
            print(new)
            res.next = new
            res = res.next
            
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            val = (l1.val + add) % 10
            add = 1 if l1.val + add >= 10 else 0
            new = ListNode(val)
            res.next = new
            res = res.next
            l1 = l1.next
        while l2 is not None:
            val = (l2.val + add) % 10
            add = 1 if l2.val + add >= 10 else 0
            new = ListNode(val)
            res.next = new
            res = res.next
            l2 = l2.next
        print(add)
        if add:
            new = ListNode(1)
            res.next = new
            res = res.next
        
        return head.next
        