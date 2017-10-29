# coding=utf-8
'''

48. Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for b in matrix:
            print(b)
        length = len(matrix)
        for i in range(int(length/2)):
            count = 0
            for j in range(i,length-1-i):

                matrix[i][j], matrix[i+count][length-i-1], matrix[length-i-1][length-j-1], matrix[length-j-1][i] = \
                matrix[length-j-1][i], matrix[i][j], matrix[i+count][length-i-1], matrix[length-i-1][length-j-1]

                count += 1

        print(matrix)
        #
        print('=============')
        for a in matrix:
            print(a)

mat = [[i for i in range(3)] for j in range(3)]
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
mat = [[1]]
s = Solution()
s.rotate(mat)
