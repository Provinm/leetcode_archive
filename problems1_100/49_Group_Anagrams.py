# coding=utf-8

'''
49. Group Anagrams
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.

'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dct = {}
        for i in strs:
            s = ''.join(sorted(list(i)))
            tem = dct.setdefault(s, [])
            tem.append(i)

        lst = []
        for v in dct.values():
            lst.append(v)

        return lst


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
r = s.groupAnagrams(strs)
print(r)
