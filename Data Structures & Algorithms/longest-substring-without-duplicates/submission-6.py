class Solution:
    def __init():
        pass

    def calculate_length(self, s: str) -> int:
        if len(s) == 1:
            length = 1
            return length
        dictionary = []
        length = 0
        for i in s:
            if i in dictionary:
                break
            else:
                dictionary.append(i)
                length += 1

        return length

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        max_length = 0
        for i in range(len(s)):
            for t in range(len(s)):
                if t > i:
                    length_1 = self.calculate_length(s[i: t+1])
                    max_length = max(max_length, length_1)
                else:
                    continue
        return max_length