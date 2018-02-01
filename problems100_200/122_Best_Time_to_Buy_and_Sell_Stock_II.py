#coding=utf-8
'''

122. Best Time to Buy and Sell Stock II


Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0

        cur_num = min_num = prices.pop(0)
        res = 0
        while prices:
            p = prices.pop(0)
            if p >= cur_num:
                if p-cur_num + res < p - min_num:
                    res = p-min_num
                else:
                    res += p-cur_num
                cur_num = p
            else:
                if p < min_num:
                    cur_num = min_num = p

                else:
                    cur_num = p
                

        return res

lst = range(10)
import random
random.shuffle(lst)
l = random.sample(lst, 6)
# l = [1, 6, 2, 0, 8, 5]
# l = [0, 7, 9, 5, 8, 4]
print(l)

s = Solution()
r = s.maxProfit(l)

print(r)