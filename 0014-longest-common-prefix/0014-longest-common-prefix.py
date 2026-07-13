class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = float('inf')
        for s in strs:
            if len(s) < min_str:
                min_str = len(s)
        i = 0
        while i < min_str:
            for s in strs:
                if s[i] != strs[0][i]:
                    return(s[:i])
            i += 1
        return(s[:i])
        