#coding=utf-8

'''
131. Palindrome Partitioning


Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]

'''

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        if not s:
            return [[]]
        res = []
        for idx, item in enumerate(s):
            cur_s = s[:idx+1]
            if self.is_p(cur_s):
                r = self.partition(s[idx+1:])
                for sub_item in r:
                    res.append([cur_s] + sub_item)

        return res

    def is_p(self, s):

        return s == s[::-1]  


s = Solution()
r = s.partition("aab")
print(r)


## 深度优先算法

