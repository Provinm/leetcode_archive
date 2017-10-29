# coding=utf-8

'''
4 Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        if self.median(nums2) and self.median(nums1):
            val_1 = self.median(nums1)
            val_2 = self.median(nums2)
            # print val_1,val_2
            return (val_1 + val_2) / 2
        elif self.median(nums2):
            return self.median(nums2)
        elif self.median(nums1):
            return self.median(nums1)
        else:
            return 0

    def median(self, lst):
        num = len(lst) // 2
        if len(lst) % 2 == 0:
            median_num = (float(lst[num]) + float(lst[num-1])) / 2 if len(lst) > 0 else None
        else:
            median_num = float(lst[num])
        return median_num

s1 = [3]
s2 = [1,2]

s = Solution()
res = s.findMedianSortedArrays(s1, s2)
print(res)
