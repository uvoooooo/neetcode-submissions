class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        output = 0

        while left <= right:
            mid = left + (right - left) // 2
            print(f"mid is {mid}")

            total = sum([(x + mid - 1) // mid for x in piles])
            print(f"total is {total}")
            if total < h:
                
                output = mid
                print(f"output is {output}")
                right = mid - 1
            elif total == h:
                output = mid
                print(f"output is {output}")
                right = mid - 1
            else:
                left = mid + 1

        return output 



                
                


        