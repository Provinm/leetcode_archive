# coding=utf-8
'''

47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) <= 1:
            return [nums]

        else:
            return self.per(nums, f=[], l=nums, res=[], deepth=0)

    def per(self, nums, f, l, res, deepth):


        if len(l) == 2:

            if l[0] != l[1]:
                res.append(f+l[::-1])
            res.append(f+l)

        tem = []
        for i in range(len(l)):
            if l[i] in tem:
                continue
            else:
                tem.append(l[i])
            new_nums = l
            new_nums[0], new_nums[i] = new_nums[i], new_nums[0]
            deepth += 1
            self.per(nums,f+[new_nums[0]],new_nums[1:], res, deepth)
            deepth -= 1

        return res

s = Solution()
r = s.permuteUnique([1,2,1,2,3])
print(r)
print(len(r))

r2 = [[1,1,2,2,3],[1,1,2,3,2],[1,1,3,2,2],[1,2,1,2,3],[1,2,1,3,2],[1,2,2,1,3],[1,2,2,3,1],[1,2,3,1,2],[1,2,3,2,1],[1,3,1,2,2],[1,3,2,1,2],[1,3,2,2,1],[2,1,1,2,3],[2,1,1,3,2],[2,1,2,1,3],[2,1,2,3,1],[2,1,3,1,2],[2,1,3,2,1],[2,2,1,1,3],[2,2,1,3,1],[2,2,3,1,1],[2,3,1,1,2],[2,3,1,2,1],[2,3,2,1,1],[3,1,1,2,2],[3,1,2,1,2],[3,1,2,2,1],[3,2,1,1,2],[3,2,1,2,1],[3,2,2,1,1]]
print(len(r2))
