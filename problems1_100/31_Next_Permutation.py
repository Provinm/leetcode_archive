# coding=utf-8
# author = zhouxin
# date = 2017.7.24

'''
31. Next Permutation
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        思路：
        开始的时候没读懂题目，大概意思是说，现在有一个数组，可以看作一个整数 [1,2,3] >> 123 ，
        找到这个数组的下一种排列方式，即形成的整数刚好比原数组大 123 >> 132 这里用了刚好，
        可以理解为， 将 123 随机组合，然后按小到大的顺序排列，找出目前数组下一种排列方式。
        如果该种排列方式形成的数组最大，则输出最小的排列。

        从后先前遍历数组，如果当前数字索引 i 比下一数字索引 i-1 大，则在 i 之前的数组中寻找 大于 i-1
        但小于 i 的索引 j
        交换 i-1 和 j 的位置
        最后对 i 之后的数从小到大排序
        
        """
        if len(nums) < 2 : return
        idx = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                r = self.find_right(nums[i-1], nums[i], i, nums[i+1:])
                nums[r], nums[i-1] = nums[i-1], nums[r]
                idx = i
                break
        for i in range(idx,len(nums)):
            for j in range(idx, len(nums)-1):
                if nums[j+1] < nums[j]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

    def find_right(self, left, right, idx, lst):
        if not lst:
            return idx
        suit = right
        id = idx
        for i in range(len(lst)):
            if lst[i] > left and lst[i] < right and lst[i] < suit:
                suit = lst[i]
                id = idx + i + 1

        return id

nums = [9,1]
s = Solution()
s.nextPermutation(nums)
