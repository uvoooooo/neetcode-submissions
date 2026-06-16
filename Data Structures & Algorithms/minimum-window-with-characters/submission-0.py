class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freq_t = {}
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1
        
        left = 0
        min_len = float('inf')
        shortest = ""

        # 右指针遍历
        for right in range(1, len(s) + 1):
            # 内部循环：尝试收缩左指针 left
            while left < right:
                # 1. 重新生成当前窗口的频率表 (效率极低，但符合你的要求)
                current_string = s[left : right]
                freq_current = {}
                for x in current_string:
                    freq_current[x] = freq_current.get(x, 0) + 1
                
                # 2. 检查是否完全覆盖
                is_covered = True
                for char, count in freq_t.items():
                    if freq_current.get(char, 0) < count:
                        is_covered = False
                        break
                
                if is_covered:
                    # 如果覆盖了，尝试记录最小值并右移 left 来缩小窗口
                    if len(current_string) < min_len:
                        min_len = len(current_string)
                        shortest = current_string
                    left += 1 
                else:
                    # 如果不覆盖，说明减过头了或者还没到位，停止收缩 left
                    break
        
        return shortest
            


