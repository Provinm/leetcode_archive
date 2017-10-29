# coding=utf-8
# author = zhouxin
# date = 2017.7.19

'''
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        思路：
        首先将数组从小到大排序
        从左开始遍历，直到倒数第 3 位
        确定一个左探针 为当前位置+1，确定一个右探针，为最末位置 j
        判断当前索引位 i , i+1 , j 三数之和，
        如果等于0 则将这三个数添加到 结果中
        如果大于0 则将右探针减一
        如果小于0 则将左探针 +1
        注意去重的处理

        """
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif s < 0:
                    left += 1

                else:
                    right -= 1

        return res

lst = [-1, -1, -1, 1, 1, 1, 0, 0, 0]
s = Solution()
res = s.threeSum(lst)
print(res)
