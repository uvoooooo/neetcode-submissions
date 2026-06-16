class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_length = 0

        for right in range(1, len(s) + 1):
            frequency = {}
            for i in s[left: right]: 
                frequency[i] = frequency.get(i, 0) + 1
            t = max(frequency.values())
            if len(s[left: right]) - t > k:
                left += 1
            else:
                max_length = max(max_length, len(s[left: right]))

        return max_length

        