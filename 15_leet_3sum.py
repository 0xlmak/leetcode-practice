from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the input in ascending order
        nums.sort()
        # set the output 
        result: List[List[int]] = []
        # when nums is void return nothing
        if not len(nums):
            return result
        # iterate over nums to set the sum's first term
        for i in range(len(nums) -1):
            # find all the pairs whose sums is in nums 
            maps =set()
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in maps:
                    # condition to avoid duplicate triplets
                    if [nums[i], nums[j], -(nums[i] + nums[j])] not in result:
                        result.append([nums[i], nums[j], -(nums[i] + nums[j])])
                else:
                    maps.add(nums[j])
        return result
