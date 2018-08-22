'''

152. Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

'''

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        if not nums:
            return 0

        num_max = tmp_max = nums.pop(0)
        while nums:
            num = nums.pop(0)
            if num == 0:
                num_max = max([num_max, 0, self.maxProduct(nums)])
                tmp_max = 1

            else:
                tmp_max *= num
                num_max = max([num, tmp_max, num_max])
                tmp_max = num_max

        return num_max



l = [1111,3,5,0,5,7,-1,9]
l = [2, 3, -2, 4]
# l = [-2, 0, -1]
# l = [-2, 5, -2, -4, 3]
s = Solution()
r = s.maxProduct(l)
print(r)
