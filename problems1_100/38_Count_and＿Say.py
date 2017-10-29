# coding = utf-8

'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        return self.c2c(n)

    def c2c(self, n, s=1, res='1'):
        if s == n:
            return res
        s += 1
        res += '*'
        length = len(res)
        idx = 0
        r = ''
        while idx < length-1:
            # print(idx)
            # print(res)
            nowidx = idx
            while res[idx] == res[idx+1]:
                print(idx)
                idx += 1

            idx += 1
            r += str(idx-nowidx) + res[nowidx]

        return self.c2c(n, s, r)



s = Solution()
r = s.countAndSay(5)
print(r)
