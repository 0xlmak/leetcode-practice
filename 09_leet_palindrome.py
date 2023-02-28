from typing import List

class Solution(object):
    def isPalindrome(self, x: List[int]) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        # convert integer input to string
        x_lst: str = str(x)
        # set the reversed version of the input as a string
        reverse_x_lst: str = ''
        for i in range(len(x_lst)-1, -1, -1):
            reverse_x_lst += x_lst[i]

        # compare strings of the integer input and its reversed to determine whether it is a palindrome or not
        return x_lst == reverse_x_lst