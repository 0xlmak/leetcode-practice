from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i: int = 1  # initialize nums tracker
        # iterate over nums
        while i < len(nums):
            # if a duplicate is found remove the most recent element
            if nums[i] == nums[i - 1]:
	            nums.pop(i)
            else:
                i += 1
        # return the resulting nums 
        return len(nums)
