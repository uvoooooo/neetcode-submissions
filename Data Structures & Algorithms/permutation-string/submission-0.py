class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_len = len(s1)
        # 1. 先准备好目标频率字典
        frequency_dict = {}
        for i in s1:
            frequency_dict[i] = frequency_dict.get(i, 0) + 1

        # 2. 遍历 s2，每次取长度为 target_len 的子串
        for i in range(len(s2) - target_len + 1):
            sub_string = s2[i : i + target_len]  # 取出子串

            # 3. 统计这个子串的频率
            current_dict = {}
            for char in sub_string:
                current_dict[char] = current_dict.get(char, 0) + 1

            # 4. 直接比较字典
            if current_dict == frequency_dict:
                return True
        
        return False