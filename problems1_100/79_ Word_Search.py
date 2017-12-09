
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

'''

class Solution(object):
    Routes = []
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        for i in self.get_first_pos(board, word[0]):
            next_pos = i
            if self.sub_exist(next_pos, board, word, tem=[next_pos]):
                return True
        return False

    def sub_exist(self, ini, board, word, tem, deep=1):
        print('deep={}, tem={}'.format(deep, tem))
        if not word[deep:]:
            return True

        tem_r = self.get_next_pos(board, word[deep], ini, tem)
        # print('ini={}, tem_r={}'.format(ini, tem_r))
        if not tem_r: 
            return False
        for i in tem_r:
            deep += 1
            tem.append(i)
            if self.sub_exist(i, board, word, tem, deep):
                return True
            
            deep -= 1
            tem = tem[:deep]


    def get_first_pos(self, board, word):
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word:
                    yield (row, col)

    def get_next_pos(self, board, word, pos, tem):
        row, col = pos
        left, top = (row, col-1), (row-1, col)
        right, down = (row, col+1), (row+1, col)

        res = []
        for p in [i for i in [left, top, right, down] if self.valid_pos(board, i)]:
            if board[p[0]][p[1]] == word and p not in tem:
                res.append(p)
        
        return res

    def valid_pos(self, board, pos):
        
        max_row = len(board)
        max_col = len(board[0])

        row, col = pos

        if  0 <= row < max_row and \
            0 <= col < max_col:
            return True

        else:
            return False
             

s = Solution()

board = [["A","B","C","E"],
         ["S","F","E","S"],
         ["A","D","E","E"]]

word = "ABCESEEEFS"

print(s.exist(board, word))