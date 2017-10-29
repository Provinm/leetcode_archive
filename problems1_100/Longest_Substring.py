# coding=utf-8

'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question.

'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_str = ''
        tem_str = ''
        for i in list(s):

            if i not in tem_str:
                tem_str += i

            else:
                idx = tem_str.index(i)
                tem_str = tem_str[idx+1:] + i

            if len(tem_str) > len(max_str):
                max_str = tem_str

            # print('this is tem:', tem_str)
            # print('this is max:', max_str)

        return max_str


s = Solution()
res = s.lengthOfLongestSubstring('xdpwwkew')
print('this is res',res)

