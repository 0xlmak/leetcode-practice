from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # move incrementally the last element to the top at each k step  
        for m in range(1, k + 1):
            for i in range(len(nums)-1, 0, -1):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        return None
