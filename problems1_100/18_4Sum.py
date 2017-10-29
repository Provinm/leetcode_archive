# coding=utf-8
# author = zhouxin
# date = 2017.7.21

'''
18. 4Sum
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''

class Solution(object):
    def fourSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        nums.sort()
        return self.nSum(nums, 4, target)

    def nSum(self, nums, N, target):

        if N == 2:
            return self.twoSum(nums, target)

        else:
            res = []
            for i in range(len(nums)-N+1):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                res_ = self.nSum(nums[i+1:], N-1, target-nums[i])
                for j in res_:
                    res.append([nums[i]]+j)

            return res

    def twoSum(self, nums, target):
        left = 0
        right = len(nums)-1
        res = []
        while left < right:
            if target == nums[left] + nums[right]:
                res.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left > 0 and left < right and nums[left] == nums[left-1]:
                    left += 1
                while right < len(nums)-1 and right > left and nums[right] == nums[right+1]:
                    right -= 1

            elif target > nums[left] + nums[right]:
                left += 1

            else:
                right -= 1
        # print(res)
        return res


lst = [-1,-1,-1,0,0,0,1,1,1]
lst.sort()
s = Solution()
res = s.fourSum(lst,1)
# res = s.twoSum(lst,0,[])
print(res)
