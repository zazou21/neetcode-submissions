# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        ptr=head
        while ptr :
            ptr=ptr.next
            count+=1
        ptr=head
        if count-n==0:
            return head.next
        for i in range(count-1):
            if i+1 == count-n:
                ptr.next=ptr.next.next
                return head
            ptr=ptr.next
            
                

        
       




        