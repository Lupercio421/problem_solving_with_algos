from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.mergeList(lists[i-1], lists[i])
        
        return lists[-1]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
    
solution = Solution()

#Create 1st linked-list
list1_node1 = ListNode(1)
list1_node2 = ListNode(2)
list1_node3 = ListNode(3)
list1_node1.next = list1_node2
list1_node2.next = list1_node3
list1_head = list1_node1

#Create second linked-list
list2_node1 = ListNode(1)
list2_node2 = ListNode(3)
list2_node3 = ListNode(5)
list2_node1.next = list2_node2
list2_node2.next = list2_node3
list2_head = list2_node1

#create the 3rd linked-list
list3_node1 = ListNode(3)
list3_node2 = ListNode(6)
list3_node1.next = list3_node2
list3_head = list3_node1

combinedList = []
combinedList.append(list1_head)
combinedList.append(list2_head)
combinedList.append(list3_head)

solution.mergeKLists(combinedList)