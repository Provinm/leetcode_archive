#coding=utf-8

'''

136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

'''
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        idx = 1

        while idx < len(nums):

            if nums[idx] != nums[idx-1]:
                return nums[idx-1]

            else:
                idx += 2

        else:
            return nums[-1]


    def _singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumof = 0
        i = 0
        while i < len(nums):
            sumof = sumof^nums[i]
            print(sumof)
            i = i+1
            
        return sumof
            


nums = [2,1,2]
s = Solution()
r = s._singleNumber(nums)

print(r)