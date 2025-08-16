class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:   # cookie satisfies child
                i += 1
            j += 1
        return i