from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        id1: int = 0  # first tracker to find the first index
        id2: int = 0  # second tracker to find the second index
        found: bool = False  # boolean to track when the index pair is found
        result: List[int] = []

        # loop over the list as a reference until the second index is found
        while id1 < len(nums) and found is False:
            # loop over the diff with the target until the ref is found
            while id2 < len(nums) and found is False:
                if (id2 != id1) and (nums[id1] + nums[id2] == target):
                    result.append(id1)
                    result.append(id2)
                    break
                id2 = id2 + 1
            # if nothing is found go over the next ref and reset the loop
            id1 = id1 + 1
            id2 = 0
        return result
