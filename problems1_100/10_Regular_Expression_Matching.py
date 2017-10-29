# coding=utf-8

'''
10. Regular Expression Matching
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return True if s == '' else False
        if s == '':
            if p == '.' or p == '.*':
                return True
            else:
                return False
        probe_s = 0
        probe_p = 0
        # max_p_length = len(p)
        while probe_p < len(p)-1 :
            if probe_s == len(s)-1 and p[-1] != '*' and s[-1] != p[-1]:
                return False
            print('f probe_s is ',probe_s)
            print('f probe_p is ',probe_p)
            if s[probe_s] == p[probe_p] or p[probe_p] == '.':
                if p[probe_p+1] == '*':
                    while probe_s < len(s)-1 and s[probe_s] == s[probe_s+1]:
                        probe_s += 1
                    probe_p += 1

                if probe_p != len(p)-1:
                    probe_p += 1

                if probe_s != len(s)-1:
                    probe_s += 1



            else :
                if p[probe_p+1] == '*':
                    probe_p += 2
                else:
                    return False
            print('e probe_s is ',probe_s)
            print('e probe_p is ',probe_p)

        print('out probe_s is ',probe_s)
        print('out probe_p is ',probe_p)
        print(len(p)-1,len(s)-1)

        if probe_p == len(p)-1 and probe_s == len(s)-1:
            if s[-1] == p[-1] or p[-1] == '.' or p[-1] == '*':
                return True

            else:
                return False

        else:
            return False


s1 = "aaa"
p1 = "ab*ac*a"
p1 = 'aaac*d*'

s = Solution()
res = s.isMatch(s1, p1)
print(res)
