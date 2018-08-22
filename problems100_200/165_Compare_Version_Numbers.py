#coding=utf-8

'''

165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

'''


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        v1 = [str(int(i)) for i in version1.split(".")]
        v2 = [str(int(i)) for i in version2.split(".")]

        l_v1 = len(v1)
        l_v2 = len(v2)

        diff = ["0" for i in range(abs(l_v1 - l_v2))]
        if l_v1 > l_v2:
            v2.extend(diff)

        else:
            v1.extend(diff)

        i_v1 = int(''.join(v1))
        i_v2 = int(''.join(v2))

        if i_v1 > i_v2:
            return 1
        elif i_v1 < i_v2:
            return -1
        else:
            return 0

            
v1 = "7.5.02.4"
v2 = "7.5.3"


s = Solution()
r = s.compareVersion(v1, v2)

print(r)
