#coding=utf-8

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
		思路：
		迭代求解
		找规律
		当m,n为 2,2 时

		创建如此一个矩阵
		0 0 
		0 1

		任何一个空位到右下的路径总数等于 其右边格子和下边格子到右下的总数之和

		0 1
		1 1

		2 1
		1 1

		最后得出 2

        """
        matrix = [[0 for i in range(m)] for j in range(n)]
        matrix[n-1][m-1] = 1
        for i in range(n)[::-1]:
        	for j in range(m)[::-1]:
        		# 跳过最后一个
        		if i == n-1 and j == m-1:
        			continue
        		# 处理竖底
        		elif j == m-1:
        			matrix[i][j] = matrix[i+1][j]
        		# 处理横底
        		elif i == n-1:
        			matrix[i][j] = matrix[i][j+1]

        		else:
        			matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]

        for n in matrix:
        	print(n)


s = Solution()
r = s.uniquePaths(5,2)


