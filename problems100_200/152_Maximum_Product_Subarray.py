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
        if len(nums) == 1:
            return nums[0]
        res = None

        negetive_product = None
        positive_product = 1

        cur_product = 1
        for ele in nums:
            if ele < 0:
                if negetive_product:
                    positive_product = negetive_product * cur_product * ele
                    negetive_product = None
                else:
                    positive_product = cur_product if cur_product > positive_product else positive_product
                    negetive_product = cur_product * ele

                cur_product = 1
                res = positive_product

            elif ele == 0:
                positive_product = cur_product if cur_product > positive_product else positive_product
                negetive_product = None

            else:
                cur_product *= ele

        else:
            if not res:
                res = negetive_product or positive_product
            if cur_product != 1:
                res *= cur_product

        return res

l = [1111,3,5,0,5,7,-1,9]
s = Solution()
r = s.maxProduct(l)
print(r)