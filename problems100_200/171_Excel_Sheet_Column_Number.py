#coding=utf-8

'''

171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


'''


class Solution(object):
    
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", list(range(1, 27))))
        step = 1
        _sum = 0
        for i in s[::-1]:
            
            tmp = lst[i] * step
            _sum += tmp
            step *= 26

        return _sum


s = "ALL"

ss = Solution()
r = ss.titleToNumber(s)

print(r)


