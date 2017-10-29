# coding=utf-8

'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        return bin(int('0b'+a, base=2) + int('0b'+b, base=2))[2:]


s = Solution()
r = s.addBinary('11', '1')
print(r)
