from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def sum_two(nums, target, fixed_index):
            ind_dict = {}
            result_temp = set()
            for l in range(len(nums)):
                if l == fixed_index:
                    continue
                diff = target - nums[l]
                if diff in ind_dict and ind_dict[diff] != l:
                    result_temp.add(tuple(sorted((nums[fixed_index], nums[ind_dict[diff]], nums[l]))))
                ind_dict[nums[l]] = l
            return result_temp

        result = set()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for triplet in sum_two(nums, -nums[i], i):
                result.add(triplet)
        
        return [list(triplet) for triplet in result]
