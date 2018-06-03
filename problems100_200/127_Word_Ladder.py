#coding=utf-8

'''
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        if endWord not in wordList: return 0

        mapping = {}
        for idx, item in enumerate(wordList + [beginWord]):
            for sub_item in wordList:
                if item == sub_item: continue
                if self.is_match(item, sub_item):
                    if item in mapping:
                        mapping[item].append(sub_item)

                    else:
                        mapping[item] = [sub_item]

        bfs_list = [(1, beginWord)]

        while bfs_list:

            deepth, word = bfs_list.pop(0)
            if word not in mapping:
                continue

            sub_word_list = mapping[word]
            del mapping[word]
            for w in sub_word_list:
                if w == endWord:
                    return deepth + 1

                bfs_list.append((deepth+1, w))
        return 0

    def is_match(self, w1, w2):
        
        count = 0
        for f_char, s_char in zip(w1, w2):
            
            if f_char != s_char:
                count += 1
        return count == 1

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

s = Solution()
r = s.ladderLength(beginWord, endWord, wordList)

print(r)