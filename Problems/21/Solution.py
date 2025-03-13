'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

'''
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        soln = ListNode()

        def combineLists(l1, l2) -> ListNode:
            if l1 == None and l2 == None:
                return
            if l1 == None and l2 != None:
                next = l2
                next.next = combineLists(l1, l2.next)
            elif l1 != None and l2 == None:
                next = l1
                next.next = combineLists(l1.next, l2)
            else:
                if l1.val <= l2.val:
                    next = l1
                    next.next = combineLists(l1.next, l2)
                else:
                    next = l2
                    next.next = combineLists(l1, l2.next)
            return next
        
        soln = combineLists(list1, list2)
        return soln
'''
This solution is pretty simple because of the two lists being already sorted. The merging should also be done on the nodes themselves, not just reassigning values to nodes based on what should be in the list.

This solution uses a recursive approach to go through each node of each list, compare them and then insert the proper node into our new list.

In my solution I use a new starting node to make a new list to hold the solution, however this could be done in place by either just adding new nodes to one of the lists as it takes in the values from the other list, or repoint the 'next' member of nodes to point to existing nodes as they should enter the list, which could save on memory usage if that was more important.
'''