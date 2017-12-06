# coding=utf-8
# author = zhouxin
# date = 2017.7.23

'''
29. Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        mark = (dividend<0) is (divisor<0)
        dividend, divisor = abs(divisor), abs(dividend)
        res = 0
        square = 1
        dd = dividend
        while dividend <= divisor:
        
            if dd > divisor:
                dd = dividend
                square = 1
            
            else:
                res += square
                square += square
                divisor = divisor - dd
                dd <<= 1

        res = res if mark else -res
        return min(max(-2147483648,res),2147483647)

s = Solution()
r = s.divide(2, 3)

print(r)
