# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr=None
        nexptr=head
        while nexptr is not None:
            temp=nexptr.next
            nexptr.next=ptr
            ptr=nexptr
            nexptr=temp
        return ptr


