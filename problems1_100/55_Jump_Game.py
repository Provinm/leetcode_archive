# coding = utf-8

'''
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or nums == [0]:
            return True
        else:
            l = [i for i in range(nums[0]+1) if i <= len(nums)]
            return any([self.canJump(nums[i:]) for i in l if nums[i:] != nums])


nums1 = [3,2,1,0,4]
nums2 = [2,3,1,1,4]
nums3 = [0]
nums4 = [1]
nums5 = []
nums6 = [0,1]
nums7 = [1,0,1,0]
s = Solution()
r = s.canJump(nums2)
print(r)
# assert s.canJump(nums1) == False
# assert s.canJump(nums2) == True
# assert all([s.canJump(nums3), s.canJump(nums4), s.canJump(nums5)])
