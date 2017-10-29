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
        # mark = 1 if divisor
        if divisor == 0: return -1
        if divisor>0 and dividend>0 or divisor<0 and dividend<0:
            mark = 1
        else:
            mark = -1
        # divisor, dividend = abs(divisor), abs(dividend)
        divisor = divisor if divisor>0 else divisor-divisor-divisor
        dividend = dividend if dividend>0 else dividend-dividend-dividend

        count = 0
        new_divisor = divisor
        while True:
            # if count
            if new_divisor > dividend:
                break

            new_divisor += divisor
            count += 1

        if mark > 0:
            return count
        else:
            return mark-mark-mark
