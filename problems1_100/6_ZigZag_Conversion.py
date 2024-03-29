# coding=utf-8

'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        res = ['' for i in range(numRows)]

        index = 0
        step = 1
        for i in s:
            res[index] += i
            if index == 0:
                step = 1

            elif index == numRows -1:
                step = -1

            index += step

        return ''.join(res)

sss = 'PAYPALISHIRING'
s = Solution()
res = s.convert(sss, 3)
print(res)
