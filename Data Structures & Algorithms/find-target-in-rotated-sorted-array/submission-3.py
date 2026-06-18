class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= target < nums[mid]:
                right = mid - 1
            elif nums[mid] < target <= nums[right]:
                left = mid + 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[left] > nums[mid]:
                right = mid - 1
            else:
                return -1

        

            



        