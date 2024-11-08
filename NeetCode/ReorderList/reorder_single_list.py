from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # L0 -> L1 -> Ln-1 -> Ln
        # L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> L3...

        # if even number of nodes
        # the slow.next will be the beginning of the second half of the list

        slow, fast = head, head.next
        if (slow == None):
            print("Null")
        else:
            print(str(slow.val))
        if (fast == None):
            print("Null")
        else:
            print(str(fast.val))

        while fast and fast.next:
            slow = slow.next
            print(str(slow.val))
            fast = fast.next.next
            if (fast == None):
                print("Null")
            else:
                print(str(fast.val))

        #second half of the list
        second = slow.next
        print(str(second.val))
        slow.next = None
        prev = None 

        #start of reversing 2nd half of the list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #merge the two halves
        first = head
        second = prev
        while second:
            tmp1 = first.next
            if (tmp1 == None):
                print("Null")
            else:
                print("tmp1: " + str(tmp1.val))
            tmp2 = second.next
            if (tmp2 == None):
                print("Null")
            else:
                print("tmp2: " + str(tmp2.val))
            first.next = second
            second.next = tmp1
            first = tmp1
            if (first == None):
                print("Null")
            else:
                print(str(first.val))
            second = tmp2
            if (second == None):
                print("Null")
            else:
                print(str(second.val))

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

solution.reorderList(head=head)
