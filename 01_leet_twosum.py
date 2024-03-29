from typing import List, Optional


# class Solution:
#    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
#        for i in range(len(nums)):
#            for j in range(i + 1, len(nums)):
#                if nums[i] + nums[j] == target:
#                    return [i, j]
#        return None
class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        maps = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in maps:
                maps[nums[i]] = i
            else:
                return [i, maps[target - nums[i]]]
        return None
