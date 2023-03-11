from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        id1: int = 0  # track the 1st part of special string pairs
        id2: int = 1  # track the 2nd part of special string pairs
        s_lst: List[str] = []  # input string as a list
        num: int = 0  # conversion to integer

        for c in s:
            s_lst.append(c)
            
            
        # identify, label and convert only the special string pairs
        while id1 < len(s_lst):
            if id2 == len(s_lst):
                id2 = id1
            if s_lst[id1] == "I" and s_lst[id2] == "V":
                num += 4
                id1 += 2
                id2 += 2
            elif s_lst[id1] == "I" and s_lst[id2] == "X":
                num += 9
                id1 += 2
                id2 += 2
            elif s_lst[id1] == "X" and s_lst[id2] == "L":
                num += 40
                id1 += 2
                id2 += 2
            elif s_lst[id1] == "X" and s_lst[id2] == "C":
                num += 90
                id1 += 2
                id2 += 2
            elif s_lst[id1] == "C" and s_lst[id2] == "D":
                num += 400
                id1 += 2
                id2 += 2
            elif s_lst[id1] == "C" and s_lst[id2] == "M" and id2 < len(s_lst):
                num += 900
                id1 += 2
                id2 += 2
            else:
                if s_lst[id1] == "I":
                    num += 1
                elif s_lst[id1] == "V":
                    num += 5
                elif s_lst[id1] == "X":
                    num += 10
                elif s_lst[id1] == "L":
                    num += 50
                elif s_lst[id1] == "C":
                    num += 100
                elif s_lst[id1] == "D":
                    num += 500
                elif s_lst[id1] == "M":
                    num += 1000
                id1 += 1
                id2 += 1
        return num
