# coding=utf-8

'''
7. Reverse Integer
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or not -1*(2**32) <= x <= 2**32 -1 :
            return 0
        if x > 0:
            return self.rev_int(x)
        else:
            return -1 * self.rev_int(-1*x)

    def rev_int(self, x):
        l_int = list(reversed(str(x)))
        while not l_int[0]:
            l_int = l_int[1:]

        res_int = int(''.join(l_int))
        return res_int if -1*(2**31) <= res_int <= 2**31 -1 else 0

integer = 1563847412
s = Solution()
res = s.reverse(integer)
print(res)
