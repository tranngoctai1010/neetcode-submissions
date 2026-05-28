class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = set()
        for i in range(len(nums)):
            n = -nums[i]
            hash_map = {}
            for j in range(i + 1, len(nums), 1):
                if nums[j] in hash_map:
                    results.add(tuple(sorted([nums[i], nums[j], hash_map[nums[j]]])))
                else:
                    target = n - nums[j]
                    hash_map[target] = nums[j]

        return list(results) 