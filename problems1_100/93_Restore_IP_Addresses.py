'''

93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

'''

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        if len(s) < 4:
            return []
        if len(s) > 12:
            return []
        tem_res = self.ipadd(s)
        res = ['.'.join(i) for i in tem_res if len(i)==4]
        return res

    def ipadd(self, s):
        if not s:
            return [[]]

        res = []
        length = 3 if len(s) > 2 else len(s)
        for i in range(length):
            cur_str, remain_str = s[:i+1], s[i+1:]
            if int(cur_str) > 255:
                continue
            if len(cur_str) > 1 and cur_str.startswith('0'):
                continue
            tem = self.ipadd(remain_str)
            for item in tem:
                if len(item) > 3:
                    continue
                res.append([cur_str] + item)

        return res


st = "010010"
s = Solution()
res = s.restoreIpAddresses(st)

for i in res:
    print(i)