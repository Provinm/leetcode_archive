#coding=utf-8

'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.


'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        end_of_zero = 0
        p5 = 5

        while p5 <= n:

            end_of_zero += n // p5
            p5 *= 5

        return end_of_zero


s = Solution()
r = s.trailingZeroes(4)
print(r)
