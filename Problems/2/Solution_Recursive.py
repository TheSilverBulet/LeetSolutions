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
        soln = ListNode()
        def addNumbers(left, right, carry):
            node = ListNode()
            if left == None and right != None:
                left = ListNode(0)
            elif left != None and right == None:
                right = ListNode(0)
            elif left == None and right == None and carry == 1:
                left = ListNode(0)
                right = ListNode(0)
            elif left == None and right == None and carry == 0:
                return
            sum = left.val + right.val + carry
            node.val = sum % 10
            node.next = addNumbers(left.next, right.next, 0 if sum < 10 else 1)
            return node

        soln = addNumbers(l1, l2, 0)
        return soln
'''
This solution to the problem required some additional planning and thought before starting to write the code, but has less "gotchas" involved in the solution and is a bit more intuitive.

This solution takes a recursive approach to solving the problem where each pair of nodes is evaluated and then the next is evaluated with the carry (if any), and so on.

With this solution there is no need to know the number of nodes in each list beforehand, simply handle the case where one list is out of nodes, but the other isn't, and don't forget if both nodes are None, carry must still be accounted for.
'''