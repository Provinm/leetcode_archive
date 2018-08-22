#coding=utf-8

'''
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

'''


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        
        length = len(nums)
        
        start_pos = 0
        while start_pos < length:
            
            if nums[start_pos] <= 0:
                start_pos += 1
            else:
                break

        else:
            return 1

        min_pos = nums[start_pos]

        if min_pos != 1:
            return 1

        count = start_pos + 1
        while count < length:
            
            if nums[count] - nums[count-1] <= 1:
                count += 1

            else:
                return nums[count-1] + 1

        else:
            if count == start_pos:
                return 2 if min_pos == 1 else 1
            else:
                return nums[-1] + 1


l = [7, 8, 9, 11, 12]
# l = [3, 4, -1, 1]
# l = [1, 1000]
# l = []
# l = [0, 2, 2, 1, 1]
s = Solution()
r = s.firstMissingPositive(l)
print(r)
