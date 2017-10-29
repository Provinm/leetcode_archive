# coding = utf-8


'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution(object):


    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        s = Spiral(n)
        return s.solution()



class Spiral:

    def __init__(self, N):

        self.matrix = [[None for i in range(N)] for j in range(N)]
        self.row = 0
        self.col = 0
        self.max_row = N
        self.mark = 0

    def derection(self, mark):

        around = [
        [self.row, self.col+1],
        [self.row+1, self.col],
        [self.row, self.col-1],
        [self.row-1, self.col]
        ]

        return around[mark%4]

    def next(self):
        i = self.derection(mark=self.mark)
        if -1 not in i and self.max_row not in i:
            if self.matrix[i[0]][i[1]] is None:
                self.row,self.col = i
                return None
        self.mark += 1
        return self.next()

    def solution(self):
        for i in range(1,self.max_row**2+1):
            self.matrix[self.row][self.col] = i
            if i == self.max_row**2:
                break
            self.next()

        return self.matrix

        
