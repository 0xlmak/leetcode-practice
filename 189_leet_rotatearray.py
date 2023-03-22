from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse the input array
        nums.reverse()
        k = k % len(nums)
        # reverse the first k elements
        start = 0
        end = k - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        # reverse the last n-k elements if nums has n elements
        start = k
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return None
