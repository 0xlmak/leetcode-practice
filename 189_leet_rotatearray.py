from typing import List


def reverse(nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse the input array
        nums.reverse()
        k = k % len(nums)
        # reverse the first k elements
        reverse(nums, 0, k - 1)
        # reverse the last n-k elements if nums has n elements
        reverse(nums, k, len(nums) - 1)
        return None
