# coding = utf-8
'''

66. Plus One
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l2i = int(''.join([str(i) for i in digits]))
        return [int(j) for j in list(str(l2i+1))]


digits = [0]
s = Solution()
r = s.plusOne(digits)
print(r)
