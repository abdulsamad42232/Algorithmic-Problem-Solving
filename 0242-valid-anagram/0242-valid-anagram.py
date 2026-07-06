# anagram question
s="anagram"
t="nagaran"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count={},{}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            s_count[s[i]] = s_count.get(s[i],0) + 1
            t_count[t[i]] = t_count.get(t[i],0) + 1
        for char in s:
            if s_count[char]!= t_count.get(char,0):
                return False
        else:
            return True
            