# coding = utf-8

'''
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''

class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        s = []
        mark = 0
        end = 0
        i,j = 0,-1
        while True:

            if end == 2:
                break

            m,k = self.next_(i,j,mark)
            print(i,j)
            try:
                p = matrix[m][k]
                assert p != None
                matrix[m][k] = None
                s.append(p)
                i,j = m,k
                end = 0
            except:
                mark += 1
                end += 1
                continue

        return s

    def next_(self, i , j , mark):

        pos = [
            (i, j+1),
            (i+1, j),
            (i, j-1),
            (i-1, j)
        ]

        return pos[mark%4]

'''
大牛解法:
def spiralOrder(self, matrix):
    return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
    

'''


mat = [[i*j for i in range(1,4)] for j in range(2,5)]
s = Solution()
r = s.spiralOrder(mat)
print(r)
