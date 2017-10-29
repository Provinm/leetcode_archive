# codinh=utf-8
'''

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

# 1
1 2 3
1 3 2

# 2

2 1 3
2 3 1

# 3

3 1 2
3 2 1

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]

        else:
            return self.per(nums, f=[], l=nums, res=[], deepth=0)

    def per(self, nums, f, l, res, deepth):

        print(f,l)
        if len(l) == 2:
            res.append(f+l)
            res.append(f+l[::-1])
            # return

        for i in range(len(l)):
            print(nums)
            new_nums = l
            new_nums[0], new_nums[i] = new_nums[i], new_nums[0]
            deepth += 1
            print(new_nums)
            self.per(new_nums,f+[new_nums[0]],new_nums[1:], res, deepth)
            deepth -= 1

        return res


s = Solution()
r = s.permute([1,2,3,4])
print(r)
print(len(r))

# r = [[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,3,2],[1,4,2,3],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,3,1],[2,4,1,3],[3,2,1,4],[3,2,4,1],[3,1,2,4],[3,1,4,2],[3,4,1,2],[3,4,2,1],[4,2,3,1],[4,2,1,3],[4,3,2,1],[4,3,1,2],[4,1,3,2],[4,1,2,3]]
# r2 = [[1,2,3,4],[2,1,3,4],[2,3,1,4],[2,3,4,1],[1,3,2,4],[3,1,2,4],[3,2,1,4],[3,2,4,1],[1,3,4,2],[3,1,4,2],[3,4,1,2],[3,4,2,1],[1,2,4,3],[2,1,4,3],[2,4,1,3],[2,4,3,1],[1,4,2,3],[4,1,2,3],[4,2,1,3],[4,2,3,1],[1,4,3,2],[4,1,3,2],[4,3,1,2],[4,3,2,1]]
#

# ]
# print(len(r))
# print(len(r2))
# print(sorted(r2, key=lambda x: x[0]))
