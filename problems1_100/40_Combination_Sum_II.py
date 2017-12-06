#coding=utf-8

'''
40. Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.dfs(candidates, target)

    def dfs(self, candidates, target):
        
        if target < 0:
            return 

        elif target == 0:
            return [[]]

        tem = []
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            new_cand = candidates[i+1:]
            item = candidates[i]
            r = self.dfs(new_cand, target-item)
            if not r : continue
            for j in r:
                tem.append([item]+j)

        return tem


lst = [1, 1, 2, 5, 6, 7, 10]
tar = 8
s = Solution()
r = s.combinationSum2(lst, tar)
print(r)
