'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
'''
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            solution = ListNode(0)
            tail = solution
            carry = 0
            # Quick resolutions
            if self.determineListActualZero(l1) and self.determineListActualZero(l2):
                return l1
            elif self.determineListActualZero(l1) and not self.determineListActualZero(l2):
                return l2
            elif not self.determineListActualZero(l1) and self.determineListActualZero(l2):
                return l1
            # Find out which list has more numbers
            sizel1 = self.findListLength(l1)
            sizel2 = self.findListLength(l2)
            # Use the larger length
            fullLength = max(sizel1, sizel2)
            idx = 0
            # Loop until full length expended
            while idx < fullLength or carry != 0:
                left = l1.val if l1 is not None else 0
                right = l2.val if l2 is not None else 0
                lrs = left + right + carry
                digit = lrs % 10
                carry = lrs // 10

                tmp = ListNode(digit)
                tail.next = tmp
                tail = tail.next

                l1 = l1.next if l1 is not None else None
                l2 = l2.next if l2 is not None else None
                idx += 1
            return solution.next
        
    def findListLength(self, l: Optional[ListNode]):
        if self.determineListActualZero(l):
            return 1
        else:
            size = 0
            while l != None:
                size += 1
                l = l.next if l is not None else None
            return size

    def determineListActualZero(self, l: Optional[ListNode]):
        return l != None and l.val == 0 and l.next == None

'''
This solution to the problem was much more involved, handling different edge cases and different inputs properly. It's such a long solution in-fact that I separated some of the reused logic into helper methods to avoid the main method becoming too convoluted.

This solution iteratively solves the problem, and requires setting up a dummy node to properly traverse the items and counting all of the items in the list before actually moving onto the problem-solving of the logic, which in-turn increases the time it takes to solve the problem.

Solves the problem, just not in the most efficient way possible, and takes 40+ lines to do what the recursive solution does in 30.
'''