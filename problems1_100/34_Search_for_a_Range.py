# coding=utf-8
# author = zhouxin

'''
34. Search for a Range
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].


'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []

        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        if not res:
            return [-1, -1]

        elif len(ren) == 1:
            return [res[0], res[0]]

        else:
            return [res[0], res[-1]]
