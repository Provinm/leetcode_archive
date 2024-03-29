#coding=utf-8

'''

151. Reverse Words in a String

Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        lst = [i for i in s.split(" ") if i]
        return ' '.join(reversed(lst))


s = " the sky is blue"
ss = Solution()
r = ss.reverseWords(s)

print(r)
