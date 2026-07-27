# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        half=slow.next
        prev=None
        slow.next=None
        while half:
            tmp=half.next
            half.next=prev
            prev=half
            half=tmp
        fptr,sptr=head,prev
        while sptr:
            tmp1=fptr.next
            tmp2=sptr.next
            fptr.next=sptr
            sptr.next=tmp1
            fptr=tmp1
            sptr=tmp2




      
        