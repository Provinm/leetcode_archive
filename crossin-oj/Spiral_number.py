# coding=utf-8

'''
今天这题，看起来挺简单，实际写出来并不容易。在以前公司我曾把它做过招聘的笔试题，结果惨不忍睹，不得不拿掉。

输出如图的螺旋矩阵：

 1   2   3   4
12  13  14   5
11  16  15   6
10   9   8   7
附加题：

输入一个正整数 N，输出以 N 为边长的螺旋矩阵。（比如上图就是 N 为 4 的结果）
'''

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


s = Spiral(6)
s.solution()
