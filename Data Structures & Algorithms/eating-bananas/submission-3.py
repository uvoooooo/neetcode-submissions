class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        output = 0

        while left <= right:
            mid = left + (right - left) // 2
            total = sum([(x + mid - 1) // mid for x in piles])

            if total < h:         
                output = mid
                right = mid - 1
            elif total == h:
                output = mid
                right = mid - 1
            else:
                left = mid + 1

        return output 



                
                


        