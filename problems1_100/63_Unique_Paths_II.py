#coding=utf-8
'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # obstacleGrid[m-1][n-1] = 1
        for i in range(m)[::-1]:
        	for j in range(n)[::-1]:

        		if i == m-1 and j == n-1:
        			obstacleGrid[i][j] = 1 if obstacleGrid[i][j] == 0 else 0

        		elif obstacleGrid[i][j] == 1:
        			obstacleGrid[i][j] = 0

        		elif j == n-1:
        			obstacleGrid[i][j] = obstacleGrid[i+1][j]
        		elif i == m-1:
        			obstacleGrid[i][j] = obstacleGrid[i][j+1]

        		else:
        			obstacleGrid[i][j] = obstacleGrid[i][j+1] + obstacleGrid[i+1][j]

       	for i in obstacleGrid:
       		print(i)
       	return obstacleGrid[0][0]

l = [[0,0,0],[0,1,0],[0,0,0]]
s = Solution()
r = s.uniquePathsWithObstacles(l)
print(r)