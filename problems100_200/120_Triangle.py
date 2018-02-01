#coding=utf-8
'''
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

'''

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        # bottle - top
        for idx, cur in enumerate(triangle):
            if idx < 1:
                continue
            _last = triangle[idx-1]
            # _cur = triangle[idx]
            for _i, _ in enumerate(cur):

                if _i == 0:
                    m = _last[0]
                elif _i == len(cur)-1:
                    m = _last[-1]
                else:
                    m = min([_last[_i-1], _last[_i]])

                cur[_i] += m
            print('tri = %s', triangle)

        return min(triangle[-1]) 
                
    # 时间复杂度太高了
    #     return self.sub(triangle)[0] if triangle else 0

    # def sub(self, triangle, i=-1):

    #     if not triangle:
    #         return [0]

    #     res = []
    #     first_item = triangle[0]
    #     remain_tri = triangle[1:]
    #     ac = [i, i+1] if i >= 0 else [0]
    #     for c in ac:
    #         item = first_item[c]
    #         tem = self.sub(remain_tri, c)
    #         res.append(item + min(tem))
    #     return res
            

s = Solution()
t = [[-3],[-9,7],[3,2,-4],[4,6,-1,9],[8,1,6,6,-4],[5,-5,5,7,-7,5],[-2,8,-5,1,0,-9,-9],[9,-5,0,-4,-5,-3,5,6],[-1,-1,-1,4,-2,-3,-4,-8,-7],[-2,3,-5,-6,-3,-6,5,4,-8,-9],[-8,-1,7,9,-2,-8,-1,3,-4,5,-5]]

res = s.minimumTotal(t)

print(res)