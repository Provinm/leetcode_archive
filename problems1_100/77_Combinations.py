# coding=utf-8

'''

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''

class Solution(object):


    def combine(self, n, k):
        if k == 0:
            return [[]]
        
        tem = []
        for i in range(1, n+1):
            tem_r = self.combine(i-1, k-1)
            for pre in tem_r:
                tem.append(pre+[i])

        return tem
        # return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]

n = 4
k = 0

s = Solution()
res = s.combine(n,k)
print(res)


'''


question solved by recursion algorithm

base condition:
when k == 0, no matter what n is, it must return [[]]

recursion:

see example belows

n = 4, k = 2
[1, 2, 3, 4] --> [2] + [1]
             --> [3] + [1], [3] + [2]
             --> [4] + [3], [4] + [2], [4] + [1]

so, a combine(n,k) can divide into 1--n + combine(n-1, k-1)

[4] + [i for i in combine(3, 1)]
[3] + [i for i in combine(2, 1)]




'''