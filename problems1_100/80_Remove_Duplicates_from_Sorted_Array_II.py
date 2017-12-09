#coding=utf-8
'''
80. Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        length = len(nums)
        left = 0
        res = 1
        while left <= length-1:
            # if nums[left+1] == nums[left]:
            right = left
            print('pre left = ', left)
            while right < length-1 and nums[right] == nums[right+1]:
                  right += 1
            
            if left == right:
                left += 1
            elif right - left == 1:
                left += 2
            elif right - left > 1:
                left += 2
                if right < length-1:
                    nums[left:] = nums[right+1:]
                    length = len(nums)
                    # print(left, right, nums)
                else:
                    # print('break left = ',left)
                    break
                
                
            print('after left = ', left)
            # break
        return left

    def _removeDuplicates(self, nums):
        i = 0
        for n in nums:
            print('pre',i,n, nums)
            if i < 2 or n > nums[i-2]:
                print('-->')
                nums[i] = n
                i += 1
            print('after',i,n, nums)
        return i

'''



'''

nums = [1,1,1,2,2,3,3,3]
s = Solution()
r = s._removeDuplicates(nums)
print(r)