# coding=utf-8

'''

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].



'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        思路：
        逐一遍历列表，取 i 项和 i+1 项比较，可以合并则将第 i 项置为 none 第 i+1 项为合并结果
        最后使用列表生成取出 none 即可
        """


        intervals.sort(key=lambda x: x.start)
        i = 0
        while i < len(intervals)-1:
            f, l = intervals[i], intervals[i+1]
            if f.end > l.end:
                l.start, l.end = f.start, f.end
                intervals[i] = None
            elif l.start <= f.end <= l.end:
                l.start = f.start
                intervals[i] = None

            i += 1

        return [i for i in intervals if i]


def gen_int(lst):

    return [Interval(i,j) for i,j in lst]


# lst = [(1,2), (3,6), (8,10), (15,18)]
lst = []
s = Solution()
r = s.merge(gen_int(lst))
for i in r:
    print(i.start, i.end)
