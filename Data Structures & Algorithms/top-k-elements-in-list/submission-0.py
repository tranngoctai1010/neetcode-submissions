class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, frequence in count.items():
            bucket[frequence].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i]:
                for j in range(len(bucket[i])):
                    result.append(bucket[i][j])
                    if len(result) == k:
                        return result