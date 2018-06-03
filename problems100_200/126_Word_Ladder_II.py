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
import copy
class Solution:

    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        wordList = set(wordList)
        max_long = len(wordList)
        res = self.sub(beginWord, endWord, wordList)
        r = [len(i) for i in res]
        min_c = min(r) if r else 0
        return [i for i in res if len(i) == min_c]

    def sub(self, beginWord, endWord, wordList):

        if beginWord == endWord:
            return [[endWord]]

        if not wordList:
            return []

        res = []
        for item in wordList:
            if self.is_match(beginWord, item):
                new_wordList = copy.copy(wordList)
                new_wordList.remove(item)
                sub_res = self.sub(item, endWord, new_wordList)
                if sub_res:
                    min_len = min(map(len, sub_res))
                    sub_res = [i for i in sub_res if len(i) == min_len]
                    for i in sub_res:
                        res.append([beginWord] + i)

        return res

    def is_match(self, w1, w2):
        # check if the difference between w1 and w2 is one character
        count = 0
        for i, j in zip(w1, w2):
            if i != j:
                count += 1
        return count == 1

beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]

# beginWord = "hot"
# endWord = "dog"
# wordList = ["hot","dog","dot"]

class _Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        answers = []
        word_list = wordList
        if len(word_list) == 0: return answers
        if len(beginWord) != len(endWord): return answers
        if len(endWord) != len(word_list[0]): return answers
        if endWord not in word_list: return answers

        word_len = len(endWord)

        # group words that differ in i-th position
        i_differ_list = []
        for i in range(word_len):
            i_differ_map = {}
            for word in word_list:
                substr = word[:i]+word[i+1:]
                if substr not in i_differ_map:
                    i_differ_map[substr] = []
                i_differ_map[substr].append(word)
            i_differ_list.append(i_differ_map)
            
        
        visited = set()
        parents = {}

        def do_bfs(curr_words):
            
            for curr_word in curr_words:
                visited.add(curr_word)
            
            found = False
            next_words = set()
            while curr_words:
                curr_word = curr_words.pop()
                # find all words that differ in i-th position
                # from the current word
                for i in range(word_len):
                    substr = curr_word[:i]+curr_word[i+1:]
                    for next_word in i_differ_list[i].get(substr, []):
                        if next_word == endWord: found = True
                        if next_word not in visited:
                            if next_word not in parents: 
                                parents[next_word] = []
                            parents[next_word].append(curr_word)
                            next_words.add(next_word)
                            
            if not found and next_words:
                found = do_bfs(next_words)
            
            return found 
        
        def do_dfs(prefix):
            tail = prefix[-1]
            if tail == beginWord:
                answers.append(prefix[::-1])
            else:
                for parent in parents[tail]:
                    do_dfs(prefix + [parent])
                    
        if do_bfs(set([beginWord])):
            do_dfs([endWord])
            
        return answers

s = Solution()
r = s.findLadders(beginWord, endWord, wordList)
# print(r)
for i in r:
    print(i)