# coding=utf-8

'''
71. Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.
'''

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        res = []
        count, length = 0, len(path)
        while count < length-1:
            from_slash = [path[count]]

            while count < length-1:
                count += 1
                if path[count] == '/':
                    break
                else:
                    from_slash.append(path[count])

            res_one = ''.join(from_slash)
            if res_one == '/.' or res_one == '/':
                continue
            elif res_one == '/..':
                if res:
                    res.pop(-1)
            else:
                res.append(res_one)

        r = ''.join(res)
        return r if r else '/'
        
path = "/.name"
s = Solution()
r = s.simplifyPath(path)

print(r)