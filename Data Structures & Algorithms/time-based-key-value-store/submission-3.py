class TimeMap:
#     {
#     "foo": [
#         [1, "bar"],
#         [4, "bar2"]
#     ],
#     "alice": [
#         [2, "happy"]
#     ]
# }
    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        new = [timestamp, value]

        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append(new)

    def get(self, key: str, timestamp: int) -> str:
        try:
            left, right = 0, len(self.storage[key]) - 1
            max = ""
        except:
            return ""

        while left <= right:
            mid = left + (right - left) // 2
            if self.storage[key][mid][0] == timestamp:
                return self.storage[key][mid][1]
            elif self.storage[key][mid][0] < timestamp:
                left = mid + 1
                max = self.storage[key][mid][1]
            else:
                right = mid - 1

        return max