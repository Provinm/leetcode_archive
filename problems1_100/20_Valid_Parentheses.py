# coding=utf-8
# author = zhouxin
# date = 2017.7.22

'''
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        思路：利用了 stack 的思想（虽然我在写的时候并没有发现，看了 discuss 才知道）
        逐个添加字符到字符串 new_s 中， 遇到 反符号（ ]}) ）则和前一位比较，其和应该为 0，否则为 F
        同时去除 new_s 末尾两位
        举例：
        '[{}]'
        1 >> [     new_s=[
        2 >> {     new_s=[{
        3 >> }     new_s=[{} --去除末尾两位--> new_s=[
        4 >> ]     new_s=[]  --去除末尾两位--> new_s=''
        5 >> 结束， new_s='' 为真
        """
        dct = {
            '(': 1,
            ')': -1,
            '{': 10,
            '}': -10,
            '[': 19,
            ']': -19
        }
        new_s = ''
        for i in s:
            # print(new_s)
            num = dct.get(i)
            new_s += i
            if len(new_s)>1 and num<0:
                if num + dct.get(new_s[-2]) == 0:
                    new_s = new_s[:-2]
                else:
                    return False


        if new_s == '':
            return True
        else:
            return False


st = "[(])"
s = Solution()
print(s.isValid(st))
