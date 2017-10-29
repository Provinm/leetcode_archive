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
        # print(candidates)
        return self._rec(candidates, target)

    def _rec(self, cands, target, tem=[], res=[], deepth=0):

        for i in range(deepth, len(cands)):
            if i > deepth and cands[i] == cands[i-1]:
                continue
            t = tem[-1] if tem else 0
            if cands[i] < t:
                continue
            tem = tem[:deepth] if tem else []
            # print(tem)
            if target - cands[i] == 0:
                tem.append(cands[i])
                res.append(tem)
                break
            elif target - cands[i] > 0:

                deepth += 1
                tem.append(cands[i])
                self._rec(cands, target-cands[i], tem, res, deepth)
                deepth -= 1
            else:
                break

        return res


lst = [1, 1, 2, 5, 6, 7, 10]
tar = 8
s = Solution()
r = s.combinationSum2(lst, tar)
print(r)
