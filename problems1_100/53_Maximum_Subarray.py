# coding = utf-8

'''
53. Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur_s, max_s = nums[0],nums[0]

        for i in nums[1:]:
            cur_s = max(cur_s+i, i)
            max_s = max(max_s, cur_s)

        return max_s



nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
r = s.maxSubArray(nums)
print(r)
