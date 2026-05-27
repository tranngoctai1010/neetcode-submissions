class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        n = len(nums) / 2

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

            if hash_map[num] > n:
                return num