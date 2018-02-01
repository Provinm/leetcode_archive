#coding=utf-8

'''
119. Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

'''
        res = [1]
        for i in range(rowIndex):
            tem = []
            if res == [1]:
                res = [1,1]
            else:
                last_item = res
                for idx in range(len(last_item)-1):
                    tem.append(last_item[idx]+last_item[idx+1])
                
                res = [1] + tem + [1]

        return res