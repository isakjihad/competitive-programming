# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0,next=head)
        slow=dum
        while head:
            if head.next and head.val ==head.next.val:
                while head.next and head.val ==head.next:
                    
                    head=head.next
                
                slow.next=head.next
            else:
                slow=slow.next
            head=head.next
        return dum.next
        
