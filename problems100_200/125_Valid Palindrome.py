#coding=utf-8
'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        import string
        all_valid = string.ascii_letters + string.digits
        s = list(s)
        while s:
            f = ''
            while s:
                f = s.pop(0).lower()
                if f in all_valid:
                    break
                else:
                    f = ''

            
            l = ''
            while s:
                l = s.pop(-1).lower()
                if l in all_valid:
                    break
                else:
                    l = ''

            print(f, l)
            if all([f, l]) and f != l:
                return False

        return True


st = "A man, a plan, a canal: Panama"
st = 'a.'
s = Solution()

r = s.isPalindrome(st)

print(r)