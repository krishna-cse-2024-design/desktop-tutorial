class Solution:
    def hasCycle(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next          # Move one step
            fast = fast.next.next     # Move two steps

            if slow == fast:
                return True

        return False