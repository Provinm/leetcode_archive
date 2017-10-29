# coding = utf-8
# author = zhouxin

'''

50. Pow(x, n)

Implement pow(x, n).

'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n >= 0:
            return self.mp(x, n, res=1)
        elif n < 0:
            return self.mp(1/x, n*(-1), res=1)

    def mp(self, x, n, res):

        if n == 0:
            return res

        if n%2 == 0:
            return self.mp(x*x, n//2, res)

        else:
            res = res * x
            return self.mp(x, n-1, res)


s = Solution()
r = s.myPow(0.44528,0)
print(r)
