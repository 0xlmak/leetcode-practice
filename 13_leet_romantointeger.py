from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        id1: int = 0 # track the 1st part of special string pairs 
        id2: int = 1 # track the 2nd part of special string pairs 
        bool_s_lst: List[int] = [] # list to track special pairs 
        s_lst: List[str] = [] # input string as a list
        num: int = 0 # conversion to integer

        for c in s :
            s_lst.append(c)
            bool_s_lst.append(1) # set as false by default

        # identify, label and convert only the special string pairs
        while (id1 < len(s_lst) and id2 < len(s_lst)):
            if s_lst[id1] == 'I' and s_lst[id2] == 'V':
               num += 4
               bool_s_lst[id1] = 0
               bool_s_lst[id2] = 0
               id1 = id1 + 2
               id2 = id2 + 2
            elif s_lst[id1] == 'I' and s_lst[id2] == 'X':
               num +=9
               bool_s_lst[id1] = 0
               bool_s_lst[id2] = 0
               id1 = id1 + 2
               id2 = id2 + 2
            elif s_lst[id1] == 'X' and s_lst[id2] == 'L':
               num += 40
               bool_s_lst[id1] = 0
               bool_s_lst[id2] = 0
               id1 = id1 + 2
               id2 = id2 + 2
            elif s_lst[id1] == 'X' and s_lst[id2] == 'C':
               num += 90
               bool_s_lst[id1] = 0
               bool_s_lst[id2] = 0
               id1 = id1 + 2
               id2 = id2 + 2
            elif s_lst[id1] == 'C' and s_lst[id2] == 'D':
               num += 400
               bool_s_lst[id1] = 0
               bool_s_lst[id2] = 0
               id1 = id1 + 2
               id2 = id2 + 2
            elif s_lst[id1] == 'C' and s_lst[id2] == 'M':
               num += 900
               bool_s_lst[id1] = 0
               bool_s_lst[id2] = 0
               id1 = id1 + 2
               id2 = id2 + 2
            else:
               id1 = id1 + 1
               id2 = id2 + 1
        
        #identify, label and convert only the single string of roman numerals
        for i in range(len(bool_s_lst)) :
            if bool_s_lst[i] == 1:
               if s_lst[i] == 'I':
                  num += 1
               elif s_lst[i] == 'V':
                  num += 5
               elif s_lst[i] == 'X':
                  num += 10
               elif s_lst[i] == 'L':
                  num += 50     
               elif s_lst[i] == 'C':
                  num += 100
               elif s_lst[i] == 'D':
                  num += 500
               elif s_lst[i] == 'M':
                  num += 1000 
        return num