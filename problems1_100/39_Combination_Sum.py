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

        return self._rec(candidates, target)

    def _rec(self, cands, target, tem=[], res=[], deepth=0):

        for i in range(len(cands)):

            tem = tem[:deepth] if tem else []
            if target - cands[i] == 0:
                tem.append(cands[i])
                res.append(tem)
                break

            elif target - cands[i] > 0:
                tem.append(cands[i])
                deepth += 1
                self.rec(cands[i:], target-cands[i], tem, res, deepth)
                deepth -= 1
                # tem = []

            else:
                # deepth -= 1
                break


        return res









nums = [2]
target = 1
s = Solution()
res = s.combinationSum(nums, target)
print(res)
