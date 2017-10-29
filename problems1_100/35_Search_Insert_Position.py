# coding=utf-8
# author = zhouxin
'''
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        idx = 0
        while left <= right:
            middle = (left+right)//2
            # print('f',middle, left, right)
            if left == right and nums[middle] != target:
                return left if nums[left] > target else left+1
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle + 1
            # print('e',middle, left, right)

        return idx

nums = [3,5,7,9,10]
target = 8
s = Solution()
# res = s.searchInsert(nums, target)
# print(res)
find_idx = s.searchInsert

assert find_idx([], 2) == 0
assert find_idx([2,3,4], 1) == 0
assert find_idx([2,3,4], 3) == 1
assert find_idx([3,5,9], 7) == 2
assert find_idx([7,8,9], 11) == 3
