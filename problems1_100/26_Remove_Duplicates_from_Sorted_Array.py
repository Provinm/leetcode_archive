# coding=utf-8
'''
26. Remove Duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：
        之前没读懂题，以为是返回一个在原有基础上去除重复的list，但其实是前 n 个元素不重复即可
        比如 [1,2,2,3,4,4,5] ----> [1,2,3,4,5,*,*] *表示随便你处理

        核心： 添加标记处理重复
        举例：
        >>> 1,2,2,3
        >>> 1(p),2(i),2,3
        i 标记使用 for 循环向前移动
        p 标记不重复元素
        >>> 1,2(p/i),2,3
        >>> 1,2(p/i),2,3
        >>> 1,2(p),2(i),3
        >>> 1,2(p),2,3(i)
        >>> 1,2,2(p),3(i)
        >>> 1,2,3(p),3(i)
        """

        if len(nums)<=1: return len(nums)
        probe = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                probe += 1
                nums[probe] = nums[i]

        return probe+1

lst = [1,2,3,3,4,5,5]
s = Solution()
print(s.removeDuplicates(lst))
