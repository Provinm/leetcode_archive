#coding=utf-8

'''
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

'''

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = set(nums)
        max_len = 0
        while nums:

            n = nums.pop()
            left_n = n - 1
            right_n = n + 1
            l = 0
            r = 0
            while right_n in nums:

                nums.remove(right_n)
                right_n += 1
                r += 1

            while left_n in nums:
                
                nums.remove(left_n)
                left_n -= 1
                l += 1

            max_len = max([max_len, l+r+1])

        return max_len


l = [100, 4, 200, 1, 3, 2]
s = Solution()
print(s.longestConsecutive(l))