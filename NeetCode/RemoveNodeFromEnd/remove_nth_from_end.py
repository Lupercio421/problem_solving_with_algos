from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n>0 and head:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        #delete the link
        left.next = left.next.next
        print(str(dummy.next.val) + " " + str(dummy.next.next.val))
        return dummy.next
    
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

solution.removeNthFromEnd(head=head, n = 3)