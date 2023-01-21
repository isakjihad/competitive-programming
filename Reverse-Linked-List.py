# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(pre,curr):
            if not curr:
                return pre
            tail = rec(curr,curr.next)
            curr.next=pre
            return tail
        return rec(None,head)
    
            
        
