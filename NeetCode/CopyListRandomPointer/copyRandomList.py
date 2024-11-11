from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val) #deep copy of the node
            oldToCopy[curr] = copy
            curr = curr.next #iterate until we reach None
        
        curr = head
        while curr:
            copy = oldToCopy[curr]
            print("aaaaa " + str(copy))
            # required to set the pointers to ensure a full deep copy
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
    
solution = Solution()

# Create individual ListNodes
node1 = Node(3)
node2 = Node(7)
node3 = Node(4)
node4 = Node(5)
node5 = None

node1.next = node2
node1.random = None
node2.next = node3
node2.random = 3
node3.next = node4
node3.random = 0
node4.next = node5
node4.random = 1

head = node1
solution.copyRandomList(head=head)
# [[7,null],[13,0],[11,4],[10,2],[1,0]]