class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            print(mid)

            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        return min(nums[0],nums[-1])