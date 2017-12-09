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
        """
        :type s: str
        :rtype: str
        """

        res = ''
        indexed = []
        for idx in range(len(s)):
            # if s[idx] in indexed:
            #     continue

            if len(s[idx:]) < len(res):
                break

            idxs = self.find_last(idx, s)
            print('idx={}, idxs={}'.format(idx, idxs))
            while idxs:
                
                last_idx = idxs.pop(0)
                new_s = s[idx: last_idx+1]
                if new_s == new_s[::-1]:
                    res = new_s if len(new_s) >= len(res) else res
                    print(res)
                    indexed.append(s[idx])
                    break            
        return res

    def find_last(self, ipt, s):

        idxs = []
        for i in range(len(s)):
            if s[i] == s[ipt]:
                idxs.append(i)

        return idxs[::-1]



s = Solution()

stri = "babadada"

r = s.longestPalindrome(stri)

print(r)
