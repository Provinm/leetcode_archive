# coding=utf-8

'''
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        return self.sn(n, exc=[],col=[], tem=[], res=[], deepth=0)

    def sn(self, n, exc, col, tem, res, deepth):

        # 结束条件
        if deepth == n:
            print('res',deepth, 1, col, exc, tem, res)
            res.append(tem)
            return

        for i in range(n):

            if i not in exc and i not in col:
                print('in',deepth, i, col, exc, tem, res)
                exc = [i-1, i , i+1] if deepth != n-1 else []
                t = ['.' for i in range(n)]
                t[i] = 'Q'
                tem.append(''.join(t))
                col.append(i)
                deepth += 1
                self.sn(n, exc, col, tem, res, deepth)
                deepth -= 1

                if deepth == 0:
                    tem = []
                    col = []
                    exc = []
                else:
                    print('allalala',deepth, i, col, exc, tem, res)
                    tem = tem[:-1]
                    last_l = col[-1]
                    col = col[:-1]
                    exc = [last_l-1, last_l , last_l+1]

                print('out',deepth, i, col, exc, tem, res)

        return res


s = Solution()
r = s.solveNQueens(5)
print(r)

r2 = [["Q....","..Q..","....Q",".Q...","...Q."],["Q....","...Q.",".Q...","....Q","..Q.."],[".Q...","...Q.","Q....","..Q..","....Q"],[".Q...","....Q","..Q..","Q....","...Q."],["..Q..","Q....","...Q.",".Q...","....Q"],["..Q..","....Q",".Q...","...Q.","Q...."],["...Q.","Q....","..Q..","....Q",".Q..."],["...Q.",".Q...","....Q","..Q..","Q...."],["....Q",".Q...","...Q.","Q....","..Q.."],["....Q","..Q..","Q....","...Q.",".Q..."]]
print(r2)
