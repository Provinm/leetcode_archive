# coding=utf-8
# author=zhouxin
# date = 2017.7.22

'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    def generateParenthesis(self, n):

        """
        :type n: int
        :rtype: List[str]
        """
        count = 1
        res = ['()']

        while count<n:
            res = self.handle_s(res)
            count += 1

        print(res)
        return res

    def handle_s(self, res):

        new_res = []
        for i in res:
            count = 0
            while count<len(i):
                new = i[:count] + '()' + i[count:]
                if new in new_res:
                    count +=1
                    continue
                new_res.append(new)
                count +=1
        return new_res


# assert '(())(())' in s1
s = Solution()
s.generateParenthesis(3)
