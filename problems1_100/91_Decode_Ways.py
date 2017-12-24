'''

91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

'''

from functools import lru_cache
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s.startswith('0'):
            return 0
        return self._num(s)
    @lru_cache(maxsize=None)
    def _num(self, s):
        if not s :
            return 1

        if len(s) == 1:
            if s == '0':
                return 0
            return 1

        num_s = s[:2]
        _flag = self.is_valid(num_s)
        if _flag == 0:
            return 0
        elif _flag == 1:
            return self._num(s[1:])

        elif _flag == 2:
            return self._num(s[1:]) + self._num(s[2:])

        else:
            return self._num(s[2:])
    
    def is_valid(self, num_s):

        num = int(num_s)
        if num_s[0] == '0':
            # self.flag = True
            return 0
        elif num == 10 or num == 20:
            return 3
        elif num <= 26:
            return 2
        else:
            return 1



num = 120
s = Solution()
r = s.numDecodings(str(num))

print(r)


'''
121212

1   21212
# 12  1212

1 2  1212
1 21 212 


'''
            