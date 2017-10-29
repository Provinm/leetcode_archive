# coding=utf-8
# author = zhouxin
# date = 2017.7.20

'''
17. Letter Combinations of a Phone Number
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {
            '1': '*',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '
        }
        if len(digits) < 2:
            return dct[digits]

        res = list(dct[digits[0]])

        for i in range(1, len(digits)):
            res = self.two(res, list(dct[digits[i]]))

        return res

    def two(self, str1, str2):
        res = []
        for i in str1:
            for j in str2:
                res.append(i + j)

        return res


s = Solution()
res = s.letterCombinations('23')
print(res)
