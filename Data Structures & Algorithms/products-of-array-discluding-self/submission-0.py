class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        count = nums.count(0)

        if count == 0:
            inclusive = 1
            for i in nums:
                inclusive *= i
            output = [int(inclusive/x) for x in nums]

        elif count == 1:
            inclusive = 1
            for i in nums:
                if i == 0:
                    continue
                else:
                    inclusive *= i
                
            output = [0 if x != 0 else inclusive for x in nums]

        else:
            output = [0] * len(nums)

        

        return output

        