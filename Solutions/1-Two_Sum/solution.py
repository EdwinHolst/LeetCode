"""
Problem: 1. Two Sum
Solution: https://leetcode.com/problems/two-sum/submissions/879977086/
Date: 17 Jan 2023
"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {value: idx for idx, value in enumerate(nums)}
        for idx1, val1 in enumerate(nums):
            val2 = target-val1
            idx2 = num_dict.get(val2)
            if idx2 and idx2 is not idx1:
                return [idx1, idx2]