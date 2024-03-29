# coding = utf-8
# author = zhouxin

'''

39. Combination Sum

Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.dfs(candidates, target)

    def dfs(self, candidates, target):
        
        if target < 0:
            return 

        elif target == 0:
            return [[]]

        tem = []
        for i in range(len(candidates)):
            new_cand = candidates[i:]
            item = candidates[i]
            r = self.dfs(new_cand, target-item)
            if not r : continue
            for j in r:
                tem.append([item]+j)

        return tem

nums = []
target = 7
s = Solution()
res = s.combinationSum(nums, target)
print(res)
