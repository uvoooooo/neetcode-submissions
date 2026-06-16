class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        freq_dict = defaultdict(int)
        for i in nums:
            freq_dict[i] += 1

        sorted_d = dict(
            sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
            )
        

        return list(sorted_d.keys())[:k]