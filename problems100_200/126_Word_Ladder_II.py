#coding=utf-8
'''

126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

'''

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        res = self.sub(beginWord, endWord, wordList)
        print(res)
        r = [len(i) for i in res]
        min_c = min(r) if r else 0
        return [i for i in res if len(i) == min_c]

    def sub(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return [[endWord]]

        res = []
        for idx, w in enumerate(wordList):
            # print(beginWord, w, wordList)
            if self.is_match(beginWord, w):
                # print('mark1', beginWord, w)
                new_word_list = wordList[:]
                new_word_list.remove(w)
                remain = self.sub(w, endWord, new_word_list)
                # print('mark2', remain)s
                for word_set in remain:
                    res.append([beginWord] + word_set)
                    
        return res

    def is_match(self, w1, w2):

        # count = 0
        # for i in w1:
        #     if i in w2:
        #         count += 1

        # return count == len(w1)-1
        count = 0
        for i, j in zip(w1, w2):
            if i != j:
                count += 1
        return count == 1

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog","dot"]


s = Solution()
r = s.findLadders(beginWord, endWord, wordList)
print(r)