class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(nums)
        max_ever = 1

        current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current += 1
            elif nums[i-1] == nums[i]:
                continue
            else:
                max_ever = max(max_ever, current)
                current = 1

            max_ever = max(max_ever, current)
            
        return max_ever

        

