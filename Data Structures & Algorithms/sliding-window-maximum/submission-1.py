class Solution:
    def findLargest(self, target: List[int]) -> int:
        max_o = -100000
        for i in target:
            max_o = max(max_o, i)
        return max_o

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []

        left = 0
        right = k
        output = []

        for right in range(k, len(nums) + 1):
            sub = nums[left:right]
            x = self.findLargest(sub)
            output.append(x)
            left += 1

        
        return output

