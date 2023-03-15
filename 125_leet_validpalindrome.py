class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters from the phrase in lowercase
        clean_s: str = "".join(c for c in s.lower() if c.isalnum())
        # initialize two trackers i = 0 and j = n-i-1 = n-1
        i: int = 0
        j: int = len(clean_s) - 1
        # iterate over the cleaned string of size n till character at i equals the one at j = n-i-1
        while i != j and i < len(clean_s):
            # if character at i not equal to the one at j then return False
            if clean_s[i] != clean_s[j]:
                return False
            else:
                i += 1
                j = len(clean_s) - i - 1
        # return True if the cleaned string is empty or we properly exited the loop
        return True or not clean_s
