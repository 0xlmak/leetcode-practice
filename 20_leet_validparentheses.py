from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs: dict[str, str] = {
            "(": ")",
            "[": "]",
            "{": "}",
        }  # set bracket pairs symbols
        stack: List[str] = []  # set a stack to store every found open bracket
        for bracket in s:
            if bracket in bracket_pairs:
                stack.append(bracket)  # stack each open bracket found till a closed one
                continue
            if (
                not stack or bracket != bracket_pairs[stack.pop()]
            ):  # no open bracket or no valid pair is found
                return False
        # valid pairs were found leading to empty the stack
        return len(stack) == 0
