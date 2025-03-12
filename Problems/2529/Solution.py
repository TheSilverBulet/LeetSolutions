'''
Maximum Count of Positive Integer and Negative Integer

Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

'''

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0
        for num in nums:
            pos += 1 if num > 0 else 0
            neg += 1 if num < 0 else 0
        return max(pos, neg)

'''
The solution to this problem is really simple to solve with a for-loop.
Simply loop over every element of the list counting the number of negative numbers, and number of positive numbers, and finally return whichever is greater.

I'm sure there is a more pythonic way to do this, but as it stands this solution is very readable and very easy to understand.

There may also be other optimizations with string slices, but again this is readable and easy to understand.
'''