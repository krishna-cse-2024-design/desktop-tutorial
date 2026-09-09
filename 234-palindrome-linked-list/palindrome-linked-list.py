# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        
        # came too close to this sol but too confused about the complexity i some how fot this idea
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next


        prev=None
        current=slow
        #reverse the 2nd halp 
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node

        # compare the reversed part and the remaining part meas the first part 
        pointer2=prev
        pointer1=head
        while pointer2:
            if pointer1.val!=pointer2.val:
                return False
            pointer1=pointer1.next
            pointer2=pointer2.next

        return True

            





        