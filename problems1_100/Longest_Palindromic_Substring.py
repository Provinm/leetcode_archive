# coding=utf-8

'''
5. Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
'''


class Solution(object):

    def longestPalindrome(self, s):

        if len(s) == 1:
            return s
        if len(s) == 2 and s == s[::-1]:
            return s
        else:
            return s[0]







strin = 'hsgs'

def check(strin):
    s = Solution()
    return s.longestPalindrome(strin)

res = check(strin)
print(res)


'''
超出时间要求:

        max_str = ''
        for i in range(len(s)):
            max_tem_length = 0
            once_tem_str = ''
            in_tem_str = ''
            for j in range(i, len(s)):
                in_tem_str += s[j]
                if in_tem_str == ''.join(list(reversed(in_tem_str))):
                    print('huiwen===',in_tem_str)
                    max_tem_length = len(in_tem_str)
                    once_tem_str = in_tem_str

            if max_tem_length >= len(s) - i - 1:
                if max_tem_length >= len(max_str):
                    return once_tem_str
                else:
                    return max_str

            max_str = once_tem_str if len(once_tem_str) > len(max_str) else max_str
            print('max_str==',max_str)

        return max_str

'''
