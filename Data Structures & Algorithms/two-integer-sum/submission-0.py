class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for idx, num in enumerate(nums):
            if num in hash_map:
                return [hash_map[num], idx]

            need = target - num
            hash_map[need] = idx