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
        
        return self._subset(nums, [], 0)

    def _subset(self, nums, res, deep):
        if len(nums[deep:]) == 1:
            return res
        # res.append(r_tem)
        for i in nums[deep:]:
            left = i
            res.append([left])
            tem_lst = self._subset(nums, res, deep+1)
            print(tem_lst)
            for item in tem_lst:
                res.append([left] + item)
            deep -= 1

        return res


l = list(range(1,4))
s = Solution()
res = s.subsets(l)
print(res)