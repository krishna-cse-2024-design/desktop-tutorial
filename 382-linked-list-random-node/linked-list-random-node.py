import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        
        # Calculate the length ONCE during initialization
        curr = self.head
        while curr:
            self.length += 1
            curr = curr.next

    def getRandom(self) -> int:
        # Pick a random index based on our pre-calculated length
        idx = random.randint(0, self.length - 1)
        
        curr = self.head
        # Traverse directly to that random index
        for _ in range(idx):
            curr = curr.next
            
        return curr.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()