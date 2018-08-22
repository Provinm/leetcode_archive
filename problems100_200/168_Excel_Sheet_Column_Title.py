#coding=utf-8

'''

168. Excel Sheet Column Title


Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"


'''


class Solution(object):
    
    lst = dict(zip(list(range(1, 27)), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n > 26:
            k = n % 26
            if k:
                return self.convertToTitle(n//26) + self.lst[k]
            else:
                return self.convertToTitle((n//26)-1) + self.lst[26]
        elif n == 26:
            return self.lst[26]
        else:
            return self.lst[n%26]


s = Solution()
r = s.convertToTitle(260)
print(r)
