#coding=utf-8
'''

118. Pascal's Triangle
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if numRows < 2:
        res = []
        for i in range(numRows):
            tem = []
            if not res:
                res.append([1])
            elif len(res) == 1:
                res.append([1,1])
            else:
                last_item = res[-1]
                for idx in range(len(last_item)-1):
                    tem.append(last_item[idx]+last_item[idx+1])
                
                res.append([1] + tem + [1])

        return res

s = Solution()
res = s.generate(2)

print(res)