# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)

        if head.next == None:
            return None

        slow = head
        fast = head.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        #when we reach the end of 'fast', remove the link on the slow.next node
        slow.next = slow.next.next

        return head
    
solution = Solution()

# Create individual ListNodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Set head to the first node
head = node1

solution.deleteMiddle(head=head)