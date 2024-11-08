from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive: T: O(N) & Memory: O(N)
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        
        return newHead
        
solution = Solution()
value = [1,2,3,4,6]
head = ListNode(value)
solution.reverseList(head)