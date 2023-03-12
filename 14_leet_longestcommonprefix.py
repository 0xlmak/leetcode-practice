from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result: str = ""

        # set each character of the first string as prefix
        for i in range(len(strs[0]):
            # check if the prefix is common with other strings
            for s in strs:
                # stop when out of bounds or no character is common anymore
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result = "".join([result, strs[0][i]])  # save the prefix found
        return result
