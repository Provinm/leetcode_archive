
'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

common prefix 共同前缀
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=lambda i :len(i))
        if len(strs) == 1:
            return strs[0]
        res = ''
        for i in range(len(strs[0])):
            for each in strs[1:]:
                if strs[0][i] != each[i]:
                    return res
            res += strs[0][i]

        return res

lst = ['sss','ssr', '']
s = Solution()
res = s.longestCommonPrefix(lst)
print(res)


'''
较好的解法：

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)

'''
