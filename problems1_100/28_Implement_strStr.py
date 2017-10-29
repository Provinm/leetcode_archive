# coding=utf-8
# author = zhouxin
# date = 2017.7.23

'''
28. Implement strStr()

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except:
            return -1

        '''
        # elegant solution
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
        # shortest Solution
        return haystack.find(needle)
        '''
