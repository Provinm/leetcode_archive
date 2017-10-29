# coding=utf-8
# author = zhouxin
# date = 2017.7.19

'''
16. 3Sum Closest
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # min_sum = nums[0]+nums[1]+nums[2]
        # for i in range(len(nums)-2):
        #     s = nums[i]+nums[i+1]+nums[i+2]
        #     if abs(target-s) < abs(target-min_sum):
        #         min_sum = s
        #
        # return min_sum
        '''
        nums.sort()
        min_sum = nums[0] + nums[1] +nums[2]
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1

            while left < right:
                print(i, left, right)
                s = nums[i] + nums[left] + nums[right]
                if abs(target-s) < abs(target-min_sum):
                    min_sum = s

                if target > s:
                    left += 1
                else:
                    right -= 1

        return min_sum
        '''
        


nums = [1,2,4,8,16,32,64,128]
target = 82
s = Solution()
res = s.threeSumClosest(nums, target)
print(res)
