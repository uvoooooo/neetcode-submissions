class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            for x in range(len(nums)):
                if nums[x] == complement and x != i:
                    return sorted([i, x])
        