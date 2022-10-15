class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if len(s) < 2:
            return True

        dic = {s[0]: t[0]}

        for i in range(1,len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                if t[i] in list(dic.values()):
                    return False
                else:
                    dic.update({s[i]: t[i]})

        return True
