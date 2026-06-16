class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stackk = [] #store indexes

        for i, tem in enumerate(temperatures):
            while stackk and tem > temperatures[stackk[-1]]:
                last = stackk.pop()
                output[last] = i - last

            stackk.append(i)

        return output

