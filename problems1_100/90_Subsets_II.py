#coding=utf-8
'''
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.sub(nums)

    def sub(self, nums):
        
        if not nums:
            return [[]]

        tem_ = [[nums[0]]]
        idx = 1
        # _nums = nums[1:]
        while idx < len(nums) and nums[0] == nums[idx]:
            idx += 1
            tem_.append(tem_[-1]+[nums[0]])
        tem = []
        remain = nums[idx:]
        r = self.subsetsWithDup(remain)
        for j in r:
            tem.append(j)
            for m in tem_:
                tem.append(m+j)
        return tem

nums = [1,1,2,2]
s = Solution()
r = s.subsetsWithDup(nums)
for i in r:
    print(i)

