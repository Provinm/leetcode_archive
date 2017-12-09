# coding=utf-8

'''

33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.


'''

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        bad solution with O(N)
        if target in nums:
            return nums.index(target)
        else:
            return -1

        '''
        # binary search

        if not nums: return -1
        left, right = 0, len(nums)-1

        while left <= right:

            if nums[left] > target:
                while left <= right and nums[left] > target:
                    left += 1
            
            if nums[right] < target:
                while left <= right and nums[right] < target:
                    right -= 1

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid

            else:
                left = mid

        return -1


lst = list(range(10, 15)) + list(range(5))
lst = [1]
target = 1
s = Solution()
r = s.search(lst, target)
print(r)
