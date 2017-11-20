# coding=utf-8

'''

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


'''

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        tem = []
        tem_r = self.subsets(nums[1:])
        for item in tem_r:
            tem.append(item)
            tem.append([nums[0]]+item)
        return tem



l = list(range(1,4))
s = Solution()
res = s.subsets(l)
print(res)

'''
the question only costs me less than half an hour LOL...

same method as question 77



'''