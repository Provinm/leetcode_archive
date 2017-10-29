# coding-utf-8

'''
13. Roman to Integer
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct = {
        'M': 1000 ,
        'D': 500,
        'C': 100,
        'L': 50 ,
        'X': 10,
        'V': 5,
        'I': 1 ,
        }
        if s == '':
            return 0

        f = dct[s[0]]
        second_s = dct[s[1]] if len(s)>1 else 0
        if second_s > f:
            remain_s = s[2:] if len(s)>2 else ''
            return second_s - f + self.romanToInt(remain_s)
        else:
            remain_s = s[1:] if len(s)>1 else ''
            return f + self.romanToInt(remain_s)

s = Solution()
res = s.romanToInt('MMMCMXCIX')
print(res)


assert s.romanToInt('III') == 3
assert s.romanToInt('IV') == 4
assert s.romanToInt('VI') == 6
assert s.romanToInt('XIX') == 19
assert s.romanToInt('XLV') == 45
assert s.romanToInt('MCMLXXX') == 1980
assert s.romanToInt('CMXCIX') == 999
