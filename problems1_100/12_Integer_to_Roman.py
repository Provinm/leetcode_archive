# coding=utf-8

'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

罗马数字共有七个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)。按照下面的规则可以表示任意正整数。

'''

class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        : 解释： 使用了递归的思想每次计算最高阶结果，最后累加，比如 999 会被分为 900 + 90 + 9,分次计算，最后得到结果。
        """
        dct = {
        '1000': 'M',
        '500': 'D',
        '100': 'C',
        '50': 'L',
        '10': 'X',
        '5': 'V',
        '1': 'I',
        }
        res = ''
        if num == 0:
            return ''
        else:
            scale = 10**(len(str(num))-1)
            f_num = int(str(num)[0])
            if f_num >= 5:
                if f_num == 9:
                    d = dct[str(scale)]+dct[str(scale*10)]
                else:
                    d = dct[str(scale*5)]+dct[str(scale)]*(f_num-5)

            else:
                if f_num == 4:
                    d = dct[str(scale)]+dct[str(scale*5)]
                else:
                    d = dct[str(scale)]*(f_num)
            num = int(str(num)[1:]) if num > 10 else 0
            return d + self.intToRoman(num)


s = Solution()
res = s.intToRoman(3999)
print(res)
