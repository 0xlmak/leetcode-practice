from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res: int = 0  # maximum size of turbulent subarray
        s: int = 0  # start index of the subarray
        e: int = 0  # end index of the subarray
        if len(arr) < 2:
            res = len(arr)
        elif len(arr) == 2:
            if arr[0] == arr[1]:
                res = 1
            else:
                res = len(arr)
        elif len(arr) > 2:
            while e < len(arr) - 1:
                if arr[e - 1] > arr[e] < arr[e + 1] or arr[e - 1] < arr[e] > arr[e + 1]:
                    e += 1
                else:
                    res = max(res, e - s + 1)
                    if arr[e - 1] == arr[e] == arr[e + 1]:
                        res = 1
                    s = e
                    e += 1
            if arr[e - 2] > arr[e - 1] < arr[e] or arr[e - 2] < arr[e - 1] > arr[e]:
                res = max(res, e - s + 1)
        return res
