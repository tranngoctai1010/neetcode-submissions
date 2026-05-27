class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for chs in zip(*strs):
            if len(set(chs)) == 1:
                res += chs[0]
            else:
                break
        return res