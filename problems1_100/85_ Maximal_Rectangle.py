#coding=utf-8

'''
85. Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

'''

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        row_length = len(matrix)
        col_length = len(matrix[0])
        step = []
        for row in range(row_length):
            line = matrix[row]
            step.append(self.one_line(line))

        print(step)
        res = {}
        while step:
            line = step.pop(0)
            for i in line:
                # print(i)
                # res.setdefault(i, 0) += len(i)
                if i in res:
                    res[i] = res[i] + len(i)
                else:
                    res[i] = len(i)
                

        return max(res.values())
        
    def one_line(self, line):
        # print(line)
        res = []
        idx = 0
        while idx < len(line):
            
            tem = []
            while idx < len(line) and line[idx] == '1':
                tem.append(idx)
                idx += 1
            
            if len(tem) < 2:
                pass
            else:
                res.append(tuple(tem))

            idx += 1

        return res

line = [1,1,1,1,1,0,0,1,1]
line = list(map(str, line))

matrix = [line for i in range(4)]

s = Solution()
r = s.maximalRectangle(matrix)
print(r)
                    
                        
            

