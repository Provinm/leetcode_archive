'''

121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_item = None
        cur_res = 0
        while prices:
            item = prices.pop(0)
            if cur_item is None:
                cur_item = item

            else:
                _tem = item - cur_item
                if _tem > cur_res:
                    cur_res = _tem
                elif _tem > 0:
                    pass
                else:
                    cur_item = item
                    
        return cur_res
                

l = [7]
s = Solution()
res = s.maxProfit(l)
print(res)