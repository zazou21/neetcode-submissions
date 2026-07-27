# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fptr=sptr=head
        while fptr and fptr.next:
            fptr=fptr.next.next
            sptr=sptr.next
            if fptr==sptr:
                return True
        return False

        