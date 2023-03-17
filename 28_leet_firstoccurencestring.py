from typing import List, Optional


class Solution:
    def strStr(self, haystack: str, needle: str) -> Optional[int]:
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            j = 0
            while j < len(needle):
                if haystack[i + j] == needle[j]:
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
        return None
